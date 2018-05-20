import { Component, OnInit } from '@angular/core';

import { AppService } from '../../providers/app.service';

@Component({
  selector: 'checkboxes',
  templateUrl: './checkboxes.component.html',
  styleUrls: ['./checkboxes.component.less']
})
export class CheckboxesComponent implements OnInit {
  constructor(private appService: AppService) { }

  ngOnInit() {
  }

}
