import { Injectable } from '@angular/core';
import { SwPush } from '@angular/service-worker';

@Injectable({
  providedIn: 'root'
})
export class PushNotificationsProvider {
    keys = {
      publicKey: 'BDAE-eTErxN96tRKmkxxj60ebfvM7-PI1cgwNeCwgFP6oKRTOwDzvWmZ-xwdkc7dNHBbKHksQUb6-eS8bvNlMAk',
      privateKey: 'uGQra_0tEV7JgC7dLaSf4MGcY1T7j0h7MPlHfKNZYBw',
    }

    constructor(
        private swPush: SwPush,
    ) {}

    subscribe() {
      this.swPush.requestSubscription({
          serverPublicKey: this.keys.publicKey,
      })
      .then((subscription) => {
        console.log('subscription: ', subscription);
      })
      .catch((error) => {
        console.log('error: ', error);
      })
    }
}
