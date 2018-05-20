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
        });
    }

    test() {
        this.pushNotifications.test()
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
