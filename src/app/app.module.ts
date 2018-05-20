import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { ServiceWorkerModule } from '@angular/service-worker';
import { NgxChartsModule } from '@swimlane/ngx-charts';

import { AppComponent } from './app.component';
import { ChartsComponent } from './components/charts/charts.component';
import { LevelComponent } from './components/charts/level.component';
import { CheckboxesComponent } from './components/checkboxes/checkboxes.component';
import { FeelingComponent } from './components/feeling/feeling.component';
import { NotificationComponent } from './components/notification/notification.component';
import { environment } from '../environments/environment';

@NgModule({
  declarations: [
    AppComponent,
    ChartsComponent,
    CheckboxesComponent,
    FeelingComponent,
    LevelComponent,
    NotificationComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    NgxChartsModule,
    ServiceWorkerModule.register('/ngsw-worker.js', { enabled: environment.production })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
