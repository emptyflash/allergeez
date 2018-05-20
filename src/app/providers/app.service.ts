import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AppService {
  trees = [
    'Maple',
    'Mulberry',
    'Alder',
    'Pine',
    'Birch',
    'Sycamore',
    'Hickory, Pecan',
    'Cottonwood',
    'Hackberry',
    'Oak',
    'Hazelnut',
    'Willow',
    'Cedar',
    'Linden',
    'Ash',
    'Elm',
    'Walnut',
    'Sweet Gum',
    'Other Tree Pollen/Unknown',
  ];

  weeds = [
    'Ragweed',
    'Plantain',
    'Sage',
    'Sheep Sorel',
    'Aster',
    'Cattail',
    'Amaranth',
    'Nettle',
    'Sedge',
    'Other Weed Pollen',
  ];

  molds = [
    'Algae',
    'Erysiphe',
    'Alternaria',
    'Aspergillus',
    'Ascopores',
    'Periconia',
    'Basidiospores',
    'Pithomyces',
    'Cercospora',
    'Rusts',
    'Cladosporium',
    'Myxomycetes',
    'Curvularia',
    'Spegazzinia',
    'Helminthosporium',
    'Stemphilium',
    'Epicoccum',
    'Tetraploa',
    'Nigrospora',
    'Torula',
  ];

  selectedTrees = [];
  selectedWeeds = [];
  selectedMolds = [];

  constructor() { }

  toggleTree(tree: string) {
    if (!this.selectedTrees.includes(tree)) {
      this.selectedTrees.push(tree);
    } else {
      this.selectedTrees = this.selectedTrees.filter(t => t !== tree);
    }
  }

  toggleWeed(weed: string) {
    if (!this.selectedWeeds.includes(weed)) {
      this.selectedWeeds.push(weed);
    } else {
      this.selectedWeeds = this.selectedWeeds.filter(w => w !== weed);
    }
  }

  toggleMold(mold: string) {
    if (!this.selectedMolds.includes(mold)) {
      this.selectedMolds.push(mold);
    } else {
      this.selectedMolds = this.selectedMolds.filter(m => m !== mold);
    }
  }
}
