import {Injectable} from '@angular/core';
import {data} from './mock-data';
import * as _ from 'lodash';

enum Emotion {
  Happy,
  Neutral,
  Sad
}

enum Level {
  Low,
  Moderate,
  High,
  Extreme
}

interface IRecord {
  allergen_id: number;
  allergen_type: string;
  allergen_name: string;
  count: number;
  created_date: string;
}

@Injectable({
  providedIn: 'root'
})
class AppProvider {
  trees = ["Alder", "Ash", "Birch", "Cedar", "Cottonwood", "Elm", "Hackberry", "Hazelnut", "Hickory", "Linden", "Maple", "Mulberry", "Oak", "Other", "Pine", "SweetGum", "Sycamore", "Walnut", "Willow"];
  weeds = ["Amaranth", "Aster", "Cattail", "Nettle", "Other", "Plantain", "Ragweed", "Sage", "Sedge", "Sheep"];
  molds = ["Algae", "Alternaria", "Ascopores", "Aspergillus", "Basidiospores", "Cercospora", "Cladosporium", "Curvularia", "Epicoccum", "Erysiphe", "Helminthosporium", "Myxomycetes", "Nigrospora", "Periconia", "Pithomyces", "Rusts", "Spegazzinia", "Stemphilium", "Tetraploa", "Torula"];

  data: IRecord[] = data;
  dataForChart = {
    trees: [],
    weeds: [],
    mold: []
  };
  latestDate: number;

  selectedTrees = this.trees.slice();
  selectedWeeds = this.weeds.slice();
  selectedMolds = this.molds.slice();
  feeling:Emotion;

  constructor() {
    const unique = Array.from(new Set(this.data.map(this.getDate)));
    this.latestDate = Math.max(...unique);
    this.getChartData();
  }

  getDate(item: IRecord) {
    return +item['created_date'].split(',')[2].trim();
  }

  getChartData() {
    const treeNames = this.selectedTrees.map(t => t.toLowerCase());
    const weedNames = this.selectedWeeds.map(t => t.toLowerCase());
    const moldNames = this.selectedMolds.map(t => t.toLowerCase());

    // filter data by type (TREE, WEED, MOLD) and also whether it's currently in the list of selected allergens
    const typeAndIsSelected = (type, list) => this.data.filter(a => a.allergen_type === type && list.includes(a.allergen_name));

    const trees = Object.values(_.groupBy(typeAndIsSelected('TREE', treeNames), 'allergen_name'));
    const weeds = Object.values(_.groupBy(typeAndIsSelected('WEED', weedNames), 'allergen_name'));
    const mold = Object.values(_.groupBy(typeAndIsSelected('MOLD', moldNames), 'allergen_name'));

    const getChartPoint = (item: IRecord[]) => ({
      name: item[0].allergen_name,
      series: item.map(i => ({name: this.getDate(i), value: i.count}))
    });

    this.dataForChart.trees = _.sortBy(trees.map(getChartPoint), 'name');
    this.dataForChart.weeds = _.sortBy(weeds.map(getChartPoint), 'name');
    this.dataForChart.mold = _.sortBy(mold.map(getChartPoint), 'name');
  }

  getTodaysTreeLevel():Level {
    const total = this.data
      .filter(a => this.getDate(a) === this.latestDate)
      .filter(a => a.allergen_type === 'TREE')
      .map(a => a.count)
      .reduce((acc, val) => acc + val);

    console.log('tree total', total);

    // http://www.houstontx.gov/health/Pollen-Mold/numbers.html
    let level = Level.Extreme;
    if (total < 15) {
      level = Level.Low;
    } else if (total >= 15 && total < 90) {
      level = Level.Moderate;
    } else if (total >= 90 && total < 1500) {
      level = Level.High;
    }
    return level;
  }

  getTodaysWeedsLevel():Level {
    const total = this.data
      .filter(a => this.getDate(a) === this.latestDate)
      .filter(a => a.allergen_type === 'WEED')
      .map(a => a.count)
      .reduce((acc, val) => acc + val);

    console.log('weed and grass total', total);

    // http://www.houstontx.gov/health/Pollen-Mold/numbers.html
    let level = Level.Extreme;
    if (total < 10) {
      level = Level.Low;
    } else if (total >= 10 && total < 50) {
      level = Level.Moderate;
    } else if (total >= 50 && total < 500) {
      level = Level.High;
    }
    return level;
  }

  getTodaysMoldLevel():Level {
    const total = this.data
      .filter(a => this.getDate(a) === this.latestDate)
      .filter(a => a.allergen_type === 'MOLD')
      .map(a => a.count)
      .reduce((acc, val) => acc + val);

    console.log('mold total', total);

    // http://www.houstontx.gov/health/Pollen-Mold/numbers.html
    let level = Level.Extreme;
    if (total < 6500) {
      level = Level.Low;
    } else if (total >= 6500 && total < 13000) {
      level = Level.Moderate;
    } else if (total >= 13000 && total < 50000) {
      level = Level.High;
    }
    return level;
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

  setFeeling(emotion:Emotion) {
    this.feeling = emotion;
  }
}

export {
  Emotion,
  Level,
  AppProvider,
}
