from pywebpush import webpush, WebPushException
import json

def notify(user, data):
    try:
        sub_info = {
            "endpoint": user["endpoint"], 
            "keys": {
                "auth": "+tyWAzOo2MGQ5K9vPhdmOg==",
                "p256dh": "BJwBfI2DVxj36y8XgMWY6rF7+zXL4pNFzZxafULL2lI+gbzpe7z2bTilk1Ie4EiOFNHjQkIeLL7ChP67uPonD1E="
            }
        }
        webpush(sub_info, 
                data, 
                vapid_private_key="uGQra_0tEV7JgC7dLaSf4MGcY1T7j0h7MPlHfKNZYBw",
                vapid_claims={"sub": "mailto:emptyflash@gmail.com"})
    except WebPushException as ex:
        print("I'm sorry, Dave, but I can't do that: {}", repr(ex))
        # Mozilla returns additional information in the body of the response.
        if ex.response and ex.response.json():
            extra = ex.response.json()
            print("Remote service replied with a {}:{}, {}", extra.code, extra.errno, extra.message)

if __name__ == "__main__":
    notify({"endpoint": "https://fcm.googleapis.com/fcm/send/dCt_rrO74Mk:APA91bEtUDr1Bn0BktIBacwjdSLh1rIsLAivgJThLGlFwTBhBw5LaABeHaP8y3XgeHSrMGzaEcds3MBTZf_d3GTrja3HUael1a_cczrF3Ftp2CYGBxh0mlYUQFdPa-U2cbn6_k67tVeK"}, json.dumps({"notification": {
            "title": "Angular News",
            "body": "Newsletter Available!",
            "icon": "assets/main-page-logo-small-hat.png",
            "vibrate": [100, 50, 100],
            "data": {
                "primaryKey": 1
            },
            "actions": [{
                "action": "explore",
                "title": "Go to the site"
            }]
        }}))
