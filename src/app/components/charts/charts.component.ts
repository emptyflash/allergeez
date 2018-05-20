import { Component, OnInit } from '@angular/core';
import { AppProvider, Level } from '../../providers/app.provider';


@Component({
  selector: 'charts',
  templateUrl: './charts.component.html',
  styleUrls: ['./charts.component.less']
})
export class ChartsComponent implements OnInit {
  treeLevel: Level;
  weedsLevel: Level;
  moldLevel: Level;

  constructor(private appService: AppProvider) {
    this.treeLevel = appService.getTodaysTreeLevel();
    this.weedsLevel = appService.getTodaysWeedsLevel();
    this.moldLevel = appService.getTodaysMoldLevel();
  }

  ngOnInit() {
  }

}
