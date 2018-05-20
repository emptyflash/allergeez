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

@Injectable({
  providedIn: 'root'
})
class AppProvider {
  trees = ['Maple', 'Mulberry', 'Alder', 'Pine', 'Birch', 'Sycamore', 'Hickory', 'Cottonwood', 'Hackberry', 'Oak', 'Hazelnut', 'Willow', 'Cedar', 'Linden', 'Ash', 'Elm', 'Walnut', 'SweetGum', 'Other',];
  weeds = ['Ragweed', 'Plantain', 'Sage', 'Sheep', 'Aster', 'Cattail', 'Amaranth', 'Nettle', 'Sedge', 'Other',];
  molds = ['Algae', 'Erysiphe', 'Alternaria', 'Aspergillus', 'Ascopores', 'Periconia', 'Basidiospores', 'Pithomyces', 'Cercospora', 'Rusts', 'Cladosporium', 'Myxomycetes', 'Curvularia', 'Spegazzinia', 'Helminthosporium', 'Stemphilium', 'Epicoccum', 'Tetraploa', 'Nigrospora', 'Torula',];

  data = data;

  selectedTrees = this.trees.slice();
  selectedWeeds = this.weeds.slice();
  selectedMolds = this.molds.slice();
  feeling:Emotion;

  constructor() {
  }

  getTodaysTreeLevel():Level {
    const total = this.data
      // TODO - filter only data points from most recent day
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
      // TODO - filter only data points from most recent day
      .filter(a => a.allergen_type === 'WEED')
      .map(a => a.count)
      .reduce((acc, val) => acc + val);

    console.log('weed and grass total', total);

    // http://www.houstontx.gov/health/Pollen-Mold/numbers.html
    let level = Level.Extreme;
    if (total < 5) {
      level = Level.Low;
    } else if (total >= 5 && total < 20) {
      level = Level.Moderate;
    } else if (total >= 20 && total < 200) {
      level = Level.High;
    }
    return level;
  }

  getTodaysMoldLevel():Level {
    const total = this.data
      // TODO - filter only data points from most recent day
      .filter(a => a.allergen_type === 'WEED')
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
