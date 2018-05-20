# allergeez

Houston Hackathon 2018


Service Worker Demo: https://blog.angular-university.io/angular-push-notifications/
`src` - Angular frontend (generated with angular-cli)

    npm install
    ng serve
    // go to localhost:4200


### Backend
* creates empty DB
```
python MakeDB.py 
```
* fill empty DB with last five days of data
```
python Scrapper-Scrapper-populate.py
```
* to run every 30 min, pushed any update to DB
```
python Scrapper-update.py
```
* visualize for one pollenkind
```
python Scrapper-visualize.py
```