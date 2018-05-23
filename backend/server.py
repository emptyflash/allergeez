from flask import Flask, jsonify, request, g, send_from_directory, abort
from flask_cors import CORS
import pymysql
import user_notifications
from db import connect_db
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

DEVELOPMENT = os.environ.get("FLASK_ENV") == "development"

def get_db():
    '''Opens a new database connection per request.'''        
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db    

@app.teardown_appcontext
def close_db(error):
    '''Closes the database connection at the end of request.'''    
    if hasattr(g, 'db'):
        g.db.close()   

@app.route("/api/notifications", methods=['POST'])
def notifications():
    try:
        db = get_db()
        data = request.get_json()
        with db.cursor() as cursor:
            user_sql = "INSERT INTO `users` (`endpoint`, `auth`, `p256dh`) VALUES (%s, %s, %s)"
            cursor.execute(user_sql, (data["endpoint"], data["auth"], data["p256dh"]))
            db.commit()
            cursor.execute("SELECT LAST_INSERT_ID()")
            user_id = cursor.fetchone()['LAST_INSERT_ID()']

            sub_sql = "INSERT INTO `subscriptions` (`threshold`, `allergen_name`, `user_id`) VALUES"
            allergens = data["allergens"]
            threshold = data["threshold"]
            subscriptions = []
            for i, allergen_name in enumerate(allergens):
                sub_sql += "(%s, %s, %s)"
                if i == len(allergens) - 1:
                    sub_sql += ";"
                else:
                    sub_sql += ","
                subscriptions.append(threshold)
                subscriptions.append(allergen_name)
                subscriptions.append(user_id)

            cursor.execute(sub_sql, subscriptions)
            db.commit()
        return jsonify({"ok": True, "result": { "user_id": user_id } })
    except Exception as e:
        print(e)
        return jsonify({"ok": False, "error": str(e)})

@app.route("/api/summary")
def summary():
    try:
        db = get_db()
        with db.cursor() as cursor:
            for num_days in range(10):
              cursor.execute("""select * from allergens WHERE DATE(created_date) BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
              results=cursor.fetchall()
              if len(results)>0:
                    break;
            cursor.execute("""select * from allergens WHERE allergen_type = 'TREE' AND DATE(created_date) BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
            results=cursor.fetchall()
            tree_sum=0
            for res in results:
                tree_sum=tree_sum+res['count']
            cursor.execute("""select * from allergens WHERE allergen_type = 'WEED' AND DATE(created_date) BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
            results=cursor.fetchall()
            weed_sum=0
            for res in results:
                weed_sum=weed_sum+res['count']
            cursor.execute("""select * from allergens WHERE allergen_type = 'MOLD' AND DATE(created_date) BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
            results=cursor.fetchall()
            mold_sum=0
            for res in results:
                mold_sum=mold_sum+res['count']
        return jsonify({"tree_sum": tree_sum, "weed_sum": weed_sum,"mold_sum": mold_sum})
    except Exception as e:
        print(e)
        return jsonify({"ok": False, "error": str(e)})
    
@app.route("/api/fivedays")
def fivedays():
    try:
        db = get_db()
        with db.cursor() as cursor:
            for num_days in range(10):
                num_dist=cursor.execute("""select DISTINCT created_date from allergens WHERE DATE(created_date) BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
                if num_dist==5:
                    break;

            cursor.execute("""select * from allergens WHERE DATE(created_date) BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW()) ORDER BY created_date""" %num_days)
            results=cursor.fetchall()
        return jsonify(results)
    except Exception as e:
        print(e)
        return jsonify({"ok": False, "error": str(e)})

@app.route("/api/feedback", methods=["POST"])
def feedback():
    try:
        db = get_db()
        data = request.get_json()
        with db.cursor() as cursor:
            feedback_sql = "INSERT INTO `feedback` (`emotion`, `user_id`) VALUES (%s, %s)"
            cursor.execute(feedback_sql, (data["emotion"], data["user_id"]))
            db.commit()
        return jsonify({"ok": True})
    except Exception as e:
        print(e)
        return jsonify({"ok": False, "error": str(e)})


@app.route("/api/test_notification", methods=["POST"])
def test_notification():
    try:
        db = get_db()
        data = request.get_json()
        with db.cursor() as cursor:
            feedback_sql = "select * from users where id = %s"
            cursor.execute(feedback_sql, (data["user_id"],))
            user = cursor.fetchone()
            notification = user_notifications.make_notification("Hello from Allergeez!", "This is a notification")
            user_notifications.notify(user, notification)
        return jsonify({"ok": True})
    except Exception as e:
        print(e)
        return jsonify({"ok": False, "error": str(e)})
            
@app.route('/')
def root():
    if DEVELOPMENT:
        return send_from_directory("../dist/allergeez", "index.html")
    else:
        flask.abort(404)

@app.route('/<path:path>')
def dist(path):
    if DEVELOPMENT:
        return send_from_directory("../dist/allergeez", path)
    else:
        flask.abort(404)

if __name__ == "__main__":
    app.run()
