import { Component } from '@angular/core';

import { AppProvider } from '../../providers/app.provider';

@Component({
  selector: 'checkboxes',
  templateUrl: './checkboxes.component.html',
  styleUrls: ['./checkboxes.component.less']
})
export class CheckboxesComponent {
  threshold = 'low';

  constructor(
      public appService: AppProvider
  ) {}

  getAllergens() {
      return [
        ...this.appService.selectedMolds.map(a => a.toLowerCase()),
        ...this.appService.selectedTrees.map(a => a.toLowerCase()),
        ...this.appService.selectedWeeds.map(a => a.toLowerCase()),
      ];
  }
}
