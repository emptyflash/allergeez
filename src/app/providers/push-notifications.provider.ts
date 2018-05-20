import { Injectable } from '@angular/core';
import { SwPush } from '@angular/service-worker';
import { HttpClient } from '@angular/common/http';

interface ISubscriptionResponse {
    subscribed: boolean;
    message?: string;
}

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
        private http: HttpClient,
    ) {}

    subscribe(allergens, threshold) {
        return new Promise((resolve, reject) => {
            this.swPush.requestSubscription({
                serverPublicKey: this.keys.publicKey,
            }).then(({ endpoint }) => {
                  this.http.post(`https://b2238bdc.ngrok.io/notifications`, {
                      endpoint,
                      allergens,
                      threshold,
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
                        error: error,
                    });
                });
        })

    }
}
