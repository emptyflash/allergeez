import { Component, Output } from '@angular/core';
import { PushNotificationsProvider } from '../providers/push-notifications.provider';

@Component({
  selector: 'notifications-setup',
  template: `
    <div class="notifications-setup">
        <div *ngIf="message && attemptedSubscription">
            {{ message }}
        </div>
        <button (click)="setupNotifications()">
          Set Up Notifications
        </button>
    </div>
  `,
})
export class NotificationsSetupComponent {
  @Output()
  subscribed = false;
  message = '';
  attemptedSubscription = false;

  constructor(
      private pushNotifications: PushNotificationsProvider,
  ) {}

  setupNotifications() {
    this.attemptedSubscription = true;

    this.pushNotifications.subscribe().then(({ subscribed, message }) => {
        this.subscribed = subscribed;
        this.message = message;
    });
  }
}
