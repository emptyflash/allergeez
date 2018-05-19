import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ChartsComponent } from './components/Charts.component';
import { CheckboxesComponent } from './components/Checkboxes.component';
import { HowDoYouFeelComponent } from './components/HowDoYouFeel.component';
import { NotificationsSetupComponent } from './components/NotificationsSetup.component';

@NgModule({
  declarations: [
    AppComponent,
    ChartsComponent,
    CheckboxesComponent,
    HowDoYouFeelComponent,
    NotificationsSetupComponent,
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
