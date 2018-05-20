import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ChartsComponent } from './components/Charts.component';
import { CheckboxesComponent } from './components/Checkboxes.component';
import { HowDoYouFeelComponent } from './components/HowDoYouFeel.component';
import { NotificationsSetupComponent } from './components/NotificationsSetup.component';
import { PushNotificationsProvider } from './providers/push-notifications.provider';
import { ServiceWorkerModule } from '@angular/service-worker';
import { environment } from '../environments/environment';

@NgModule({
  declarations: [
    AppComponent,
    ChartsComponent,
    CheckboxesComponent,
    HowDoYouFeelComponent,
    NotificationsSetupComponent,
  ],
  imports: [
    BrowserModule,
    ServiceWorkerModule.register('/ngsw-worker.js', { enabled: environment.production })
  ],
  providers: [
      PushNotificationsProvider,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
