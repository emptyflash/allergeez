import { Component, OnInit } from '@angular/core';
import { PushNotificationsProvider } from '../../providers/push-notifications.provider';

@Component({
  selector: 'notification',
  templateUrl: './notification.component.html',
  styleUrls: ['./notification.component.less']
})
export class NotificationComponent implements OnInit {

  constructor(private pushNotifications: PushNotificationsProvider) {}

  setupNotifications() {
    this.pushNotifications.subscribe();
  }

  ngOnInit() {
  }

}
