import { Component } from '@angular/core';
import { PushNotificationsProvider } from '../providers/push-notifications.provider';

@Component({
  selector: 'notifications-setup',
  template: `
    <div class="notifications-setup">
        <button (click)="setupNotifications()">
          Set Up Notifications
        </button>
    </div>
  `,
})
export class NotificationsSetupComponent {
  constructor(
      private pushNotifications: PushNotificationsProvider,
  ) {}

  setupNotifications() {
    this.pushNotifications.subscribe();
  }
}
