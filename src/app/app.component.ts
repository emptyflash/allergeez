import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})
export class AppComponent {
  private trees = [
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
    'Other Tree Pollen/Unknown'
  ];
  private weeds = [
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
  private mold = [
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

}
