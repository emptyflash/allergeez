import { Component, Input } from '@angular/core';
import { PushNotificationsProvider } from '../../providers/push-notifications.provider';

@Component({
  selector: 'notification',
  templateUrl: './notification.component.html',
  styleUrls: ['./notification.component.less']
})
export class NotificationComponent {
    subscribed = false;
    error = '';
    attemptedSubscription = false;
    @Input()
    allergens = []
    @Input()
    threshold = '';
    hasUserId = JSON.parse(localStorage.getItem('[allergeez:userId]')) !== null;

    constructor(
        private pushNotifications: PushNotificationsProvider,
    ) {}

    setupNotifications() {
        this.attemptedSubscription = true;

        this.pushNotifications.subscribe(
            this.allergens,
            this.threshold,
        ).then(({ ok, error }) => {
            this.subscribed = ok;
            this.error = error;
            this.hasUserId = ok;
        });
    }

    test() {
        const userId = JSON.parse(localStorage.getItem('[allergeez:userId]'));

        if (!userId) return;

        this.pushNotifications.test(userId)
            .then(({ ok, error }) => {
               const message = `Push notifications are ${!ok ? 'not' : ''} working.`;
               if (!ok) {
                   alert(message);
                   console.log('error testing push notifications: ', error);
               } else {
                   alert(message);
               }
            });
    }
}
