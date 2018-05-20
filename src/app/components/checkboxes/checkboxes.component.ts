import { Component, OnInit } from '@angular/core';

import { AppProvider } from '../../providers/app.provider';

@Component({
  selector: 'checkboxes',
  templateUrl: './checkboxes.component.html',
  styleUrls: ['./checkboxes.component.less']
})
export class CheckboxesComponent implements OnInit {
  constructor(appService: AppProvider) { }

  ngOnInit() {
  }

}
