import { Component, OnInit } from '@angular/core';

import { AppProvider, Emotion } from '../../providers/app.provider';

@Component({
  selector: 'feeling',
  templateUrl: './feeling.component.html',
  styleUrls: ['./feeling.component.less']
})
export class FeelingComponent implements OnInit {
  Emotion = Emotion; // for template

  constructor(private appService: AppProvider) { }

  ngOnInit() {
  }

}
