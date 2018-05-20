# allergeez

Houston Hackathon 2018


### Frontend

`src` - Angular frontend (generated with [angular-cli](https://github.com/angular/angular-cli))

*  push notifications:
    Followed the following tutorial to get service worker and push notifications setup. Also a good read on how push notifications work.
    https://blog.angular-university.io/angular-push-notifications/

* Run site
```
npm install
ng serve
```
 Then you can go to localhost:4200


### Backend
* creates empty DB
```
python MakeDB.py 
```
* fill empty DB with last five days of data
```
python Scrapper-Scrapper-populate.py
```
* to run every 30 min, pushed any update to DB, determines when to send notifications 
```
python Scrapper-update.py
```
* determines what notifications to send to which user:
```
python User-Notifications.py
```
* visualize for one pollenkind
```
python Scrapper-visualize.py
```