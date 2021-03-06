import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import * as _ from 'lodash';

enum Emotion {
  Happy = 'happy',
  Neutral = 'neutral',
  Sad = 'sad',
}

enum Level {
  Low,
  Moderate,
  High,
  Extreme
}

interface IRecord {
  allergen_id:number;
  allergen_type:string;
  allergen_name:string;
  count:number;
  created_date:string;
}

interface ISum {
  tree_sum: number;
  weed_sum: number;
  mold_sum: number;
}

@Injectable({
  providedIn: 'root'
})
class AppProvider {
  trees = ["Alder", "Ash", "Birch", "Cedar", "Cottonwood", "Elm", "Hackberry", "Hazelnut", "Hickory", "Linden", "Maple", "Mulberry", "Oak", "Other", "Pine", "SweetGum", "Sycamore", "Walnut", "Willow"];
  weeds = ["Amaranth", "Aster", "Cattail", "Nettle", "Other", "Plantain", "Ragweed", "Sage", "Sedge", "Sheep"];
  molds = ["Algae", "Alternaria", "Ascopores", "Aspergillus", "Basidiospores", "Cercospora", "Cladosporium", "Curvularia", "Epicoccum", "Erysiphe", "Helminthosporium", "Myxomycetes", "Nigrospora", "Periconia", "Pithomyces", "Rusts", "Spegazzinia", "Stemphilium", "Tetraploa", "Torula"];

  data:IRecord[] = [];
  dataForChart = {
    trees: [],
    weeds: [],
    mold: []
  };
  latestDate:Date;
  todaysDate:Date;

  sums = {
    trees: 0,
    weeds: 0,
    mold: 0,
  };
  levels = {
    trees: 0,
    weeds: 0,
    mold: 0,
  };

  selectedTrees = this.trees.slice();
  selectedWeeds = this.weeds.slice();
  selectedMolds = this.molds.slice();
  feeling:string;

  constructor(private http:HttpClient) {
    this.todaysDate = new Date();
    this.getFiveDaysData().then((hasData) => {
      if (hasData) {
        this.http.get('/api/summary')
          .subscribe((response:ISum) => {
            const getSum = (type:string) => {
              if (this.data) {
                return this.data
                  .filter(a => this.getDate(a) === this.latestDate)
                  .filter(a => a.allergen_type === type)
                  .map(a => a.count)
                  .reduce((acc, val) => acc + val);
              } else {
                return 0;
              }
            };

            if (response) {
              this.sums.trees = response.tree_sum || getSum('TREE');
              this.sums.weeds = response.weed_sum || getSum('WEED');
              this.sums.mold = response.mold_sum || getSum('MOLD');

              this.getTodaysTreeLevel();
              this.getTodaysWeedsLevel();
              this.getTodaysMoldLevel();
            }
          });
      }
    })
  }

  getFiveDaysData() {
    return new Promise((resolve) => {
      this.http.get('/api/fivedays')
        .subscribe((response:IRecord[]) => {
          if (!Array.isArray(response)) {
              resolve(false);
              return;
          }
          this.data = response;
          const unique = Array.from(new Set(this.data.map(this.getDate)));
          this.latestDate = unique.sort((a, b) => b.getTime() - a.getTime())[0];
          this.getChartData();
          resolve(true);
        }, (error) => {
          console.error(`Couldn't load data for 5 days :(`);
          resolve(false);
        });
    });
  }

  /** Returns the date number, i.e. July 7, 2018 5:00 returns 7 **/
  getDate(item:IRecord):Date {
    return new Date(item['created_date']);
  }

  /** Transform the data to be compatible with the ngx-chart **/
  getChartData() {
    const treeNames = this.selectedTrees.map(t => t.toLowerCase());
    const weedNames = this.selectedWeeds.map(t => t.toLowerCase());
    const moldNames = this.selectedMolds.map(t => t.toLowerCase());

    // filter data by type (TREE, WEED, MOLD) and also whether it's currently in the list of selected allergens
    const typeAndIsSelected = (type, list) => this.data.filter(a => a.allergen_type === type && list.includes(a.allergen_name));

    const trees = Object.values(_.groupBy(typeAndIsSelected('TREE', treeNames), 'allergen_name'));
    const weeds = Object.values(_.groupBy(typeAndIsSelected('WEED', weedNames), 'allergen_name'));
    const mold = Object.values(_.groupBy(typeAndIsSelected('MOLD', moldNames), 'allergen_name'));

    const getChartPoint = (item:IRecord[]) => ({
      name: item[0].allergen_name,
      series: item.map((i, index) => ({name: index, value: i.count}))
    });

    this.dataForChart.trees = _.sortBy(trees.map(getChartPoint), 'name');
    this.dataForChart.weeds = _.sortBy(weeds.map(getChartPoint), 'name');
    this.dataForChart.mold = _.sortBy(mold.map(getChartPoint), 'name');
  }

  getTodaysTreeLevel() {
    // http://www.houstontx.gov/health/Pollen-Mold/numbers.html
    let level = Level.Extreme;
    if (this.sums.trees < 15) {
      level = Level.Low;
    } else if (this.sums.trees >= 15 && this.sums.trees < 90) {
      level = Level.Moderate;
    } else if (this.sums.trees >= 90 && this.sums.trees < 1500) {
      level = Level.High;
    }
    this.levels.trees = level;
  }

  getTodaysWeedsLevel() {
    // http://www.houstontx.gov/health/Pollen-Mold/numbers.html
    let level = Level.Extreme;
    if (this.sums.weeds < 10) {
      level = Level.Low;
    } else if (this.sums.weeds >= 10 && this.sums.weeds < 50) {
      level = Level.Moderate;
    } else if (this.sums.weeds >= 50 && this.sums.weeds < 500) {
      level = Level.High;
    }
    this.levels.weeds = level;
  }

  getTodaysMoldLevel() {
    // http://www.houstontx.gov/health/Pollen-Mold/numbers.html
    let level = Level.Extreme;
    if (this.sums.mold < 6500) {
      level = Level.Low;
    } else if (this.sums.mold >= 6500 && this.sums.mold < 13000) {
      level = Level.Moderate;
    } else if (this.sums.mold >= 13000 && this.sums.mold < 50000) {
      level = Level.High;
    }
    this.levels.mold = level;
  }

  toggleTree(tree:string) {
    if (!this.selectedTrees.includes(tree)) {
      this.selectedTrees.push(tree);
    } else {
      this.selectedTrees = this.selectedTrees.filter(t => t !== tree);
    }
    this.getChartData();
  }

  toggleWeed(weed:string) {
    if (!this.selectedWeeds.includes(weed)) {
      this.selectedWeeds.push(weed);
    } else {
      this.selectedWeeds = this.selectedWeeds.filter(w => w !== weed);
    }
    this.getChartData();
  }

  toggleMold(mold:string) {
    if (!this.selectedMolds.includes(mold)) {
      this.selectedMolds.push(mold);
    } else {
      this.selectedMolds = this.selectedMolds.filter(m => m !== mold);
    }
    this.getChartData();
  }

  toggleAllTrees() {
    if (this.selectedTrees.length === 0) {
      this.selectedTrees = this.trees.slice();
    } else {
      this.selectedTrees = [];
    }
    this.getChartData();
  }

  toggleAllWeeds() {
    if (this.selectedWeeds.length === 0) {
      this.selectedWeeds = this.weeds.slice();
    } else {
      this.selectedWeeds = [];
    }
    this.getChartData();
  }

  toggleAllMold() {
    if (this.selectedMolds.length === 0) {
      this.selectedMolds = this.molds.slice();
    } else {
      this.selectedMolds = [];
    }
    this.getChartData();
  }


  setFeeling(emotion:string) {
    this.feeling = emotion;

    return new Promise((resolve) => {
      localStorage.setItem('[allergeez:feeling]', this.feeling);

      this.http.post(`/api/feedback`, {
          emotion,
          user_id: JSON.parse(localStorage.getItem('[allergeez:userId]'))
        })
        .subscribe((response) => {
          resolve(response);
        }, (error) => {
          resolve({
            error,
            ok: false,
          })
        });
    })
  }
}

export {
  Emotion,
  Level,
  AppProvider,
}
