import { Injectable } from '@angular/core';
import { SwPush } from '@angular/service-worker';
import { HttpClient } from '@angular/common/http';

interface ISubscriptionResponse {
    subscribed: boolean;
    message?: string;
}

const toBase64 = (sub, key) => btoa(String.fromCharCode.apply(null, new Uint8Array(sub.getKey(key))));

@Injectable({
  providedIn: 'root'
})
export class PushNotificationsProvider {

    //generated VAPID keys with https://github.com/web-push-libs/web-push
    keys = {
      publicKey: 'BDAE-eTErxN96tRKmkxxj60ebfvM7-PI1cgwNeCwgFP6oKRTOwDzvWmZ-xwdkc7dNHBbKHksQUb6-eS8bvNlMAk',
      privateKey: 'uGQra_0tEV7JgC7dLaSf4MGcY1T7j0h7MPlHfKNZYBw',
    }

    constructor(
        private swPush: SwPush,
        private http: HttpClient,
    ) {}

    subscribe(allergens, threshold) {
        return new Promise((resolve) => {
            this.swPush.requestSubscription({
                serverPublicKey: this.keys.publicKey,
            }).then((subscription) => {
                  this.http.post(`https://692ebc1b.ngrok.io/notifications`, {
                      endpoint: subscription.endpoint,
                      allergens,
                      threshold,
                      auth: toBase64(subscription, 'auth'),
                      p256dh: toBase64(subscription, 'p256dh'),
                  }).subscribe((response: ISubscriptionResponse) => {
                      resolve(response);
                  }, (error) => {
                      console.log('error subscribing with backend: ', error);

                      resolve({
                        ok: false,
                        error: error,
                      });
                  })
                })
                .catch((error) => {
                    console.log('error setting permission on browser: ', error);

                    resolve({
                        ok: false,
                        error,
                    });
                });
        })
    }

    test() {
        return new Promise((resolve) => {
            this.swPush.requestSubscription({
                serverPublicKey: this.keys.publicKey,
            }).then((subscription) => {
                this.http.post(`https://692ebc1b.ngrok.io/test`, {
                    endpoint: subscription.endpoint,
                    auth: toBase64(subscription, 'auth'),
                    p256dh: toBase64(subscription, 'p256dh'),
                }).subscribe((response) => {
                    resolve(response);
                }, (error) => {
                    resolve({
                        ok: false,
                        error,
                    });
                });
            })
            .catch((error) => {
                resolve({
                    ok: false,
                    error,
                });
            });
        })

    }
}
