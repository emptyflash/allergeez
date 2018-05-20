import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ChartsComponent } from './components/charts/charts.component';
import { CheckboxesComponent } from './components/checkboxes/checkboxes.component';
import { FeelingComponent } from './components/feeling/feeling.component';
import { NotificationComponent } from './components/notification/notification.component';

@NgModule({
  declarations: [
    AppComponent,
    ChartsComponent,
    CheckboxesComponent,
    FeelingComponent,
    NotificationComponent,
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
