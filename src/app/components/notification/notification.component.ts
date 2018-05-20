import { Component, Input } from '@angular/core';
import { PushNotificationsProvider } from '../../providers/push-notifications.provider';

@Component({
  selector: 'notification',
  styleUrls: ['./notification.component.less'],
  template: `
    <div class="notification">
        <div *ngIf="!subscribed && attemptedSubscription">
          {{ error }}
        </div>
        <div *ngIf="subscribed && attemptedSubscription">
            Congratulations! You'll be notified.
        </div>
        <button (click)="setupNotifications()">Set Up Notifications</button>
    </div>
  `,
})
export class NotificationComponent {
    subscribed = false;
    error = '';
    attemptedSubscription = false;
    @Input()
    allergens = []
    @Input()
    threshold = '';

    constructor(
        private pushNotifications: PushNotificationsProvider,
    ) {}

    setupNotifications() {
        this.attemptedSubscription = true;

        console.log(this.allergens, this.threshold);

        this.pushNotifications.subscribe(
            this.allergens,
            this.threshold,
        ).then(({ ok, error }) => {
            this.subscribed = ok;
            this.error = error;
        });
    }
}