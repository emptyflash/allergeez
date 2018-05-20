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
        ...this.appService.selectedMolds,
        ...this.appService.selectedTrees,
        ...this.appService.selectedWeeds,
      ];
  }
}
