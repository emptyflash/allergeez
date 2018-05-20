import {Injectable} from '@angular/core';
import {data} from './mock-data';

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
  trees = ['Maple', 'Mulberry', 'Alder', 'Pine', 'Birch', 'Sycamore', 'Hickory', 'Cottonwood', 'Hackberry', 'Oak', 'Hazelnut', 'Willow', 'Cedar', 'Linden', 'Ash', 'Elm', 'Walnut', 'SweetGum', 'Other',];
  weeds = ['Ragweed', 'Plantain', 'Sage', 'Sheep', 'Aster', 'Cattail', 'Amaranth', 'Nettle', 'Sedge', 'Other',];
  molds = ['Algae', 'Erysiphe', 'Alternaria', 'Aspergillus', 'Ascopores', 'Periconia', 'Basidiospores', 'Pithomyces', 'Cercospora', 'Rusts', 'Cladosporium', 'Myxomycetes', 'Curvularia', 'Spegazzinia', 'Helminthosporium', 'Stemphilium', 'Epicoccum', 'Tetraploa', 'Nigrospora', 'Torula',];

  data: IRecord[] = data;
  latestDate: number;

  selectedTrees = this.trees.slice();
  selectedWeeds = this.weeds.slice();
  selectedMolds = this.molds.slice();
  feeling:Emotion;

  constructor() {
    const unique = Array.from(new Set(this.data.map(this.getDate)));
    this.latestDate = Math.max(...unique);
  }

  getDate(item: IRecord) {
    return +item['created_date'].split(',')[2].trim();
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
  }

  toggleWeed(weed:string) {
    if (!this.selectedWeeds.includes(weed)) {
      this.selectedWeeds.push(weed);
    } else {
      this.selectedWeeds = this.selectedWeeds.filter(w => w !== weed);
    }
  }

  toggleMold(mold:string) {
    if (!this.selectedMolds.includes(mold)) {
      this.selectedMolds.push(mold);
    } else {
      this.selectedMolds = this.selectedMolds.filter(m => m !== mold);
    }
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
