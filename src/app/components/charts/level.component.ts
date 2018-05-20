import { Component, Input } from '@angular/core';
import { Level } from '../../providers/app.provider';

@Component({
  selector: 'level',
  template: `
    <div *ngIf="level === Level.Low" class="level low">Low</div>
    <div *ngIf="level === Level.Moderate" class="level moderate">Moderate</div>
    <div *ngIf="level === Level.High" class="level high">High</div>
    <div *ngIf="level === Level.Extreme" class="level extreme">Extremely High</div>
   `,
  styleUrls: ['./level.component.less']
})
export class LevelComponent {
  @Input() level: Level = Level.Low;
  Level = Level;
}
