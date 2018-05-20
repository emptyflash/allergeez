import { Component, OnInit } from '@angular/core';

import { AppProvider, Emotion } from '../../providers/app.provider';

@Component({
  selector: 'feeling',
  templateUrl: './feeling.component.html',
  styleUrls: ['./feeling.component.less']
})
export class FeelingComponent implements OnInit {
  Emotion = Emotion; // for templatex

  constructor(
      public appService: AppProvider
  ) { }

  ngOnInit() {
  }

  addFeedback(emotion: string) {
    if (!localStorage.getItem('[allergeez:userId]')) {
      alert(`Setup for notifications first.`);
    } else {
      this.appService.setFeeling(emotion).then(({ ok, error }) => {
          if (!ok) {
              console.log('error saving feedback: ', error);
              alert(`Couldn't save your feedback`);
          } else {
              alert('Feedback saved');
          }
      });
    }
  }
}
