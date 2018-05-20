from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     db='db',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

@app.route("/notifications", methods=['POST'])
def notifications():
    try:
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


<<<<<<< HEAD
@app.route("/summary")
def summary():
=======

@app.route("/summary")
def notifications():
>>>>>>> 7e1083fc6dff6e5040ab644cd3a3426f390235b5
    try:
        with db.cursor() as cursor:
            for num_days in range(10):
              cursor.execute("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
              results=cursor.fetchall()
              if len(results)>0:
                    break;
            cursor.execute("""select * from allergens WHERE allergen_type = 'TREE' AND created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
            results=cursor.fetchall()
            tree_sum=0
            for res in results:
                tree_sum=tree_sum+res['count']
            cursor.execute("""select * from allergens WHERE allergen_type = 'WEED' AND created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
            results=cursor.fetchall()
            weed_sum=0
            for res in results:
                weed_sum=weed_sum+res['count']
            cursor.execute("""select * from allergens WHERE allergen_type = 'MOLD' AND created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
            results=cursor.fetchall()
            mold_sum=0
            for res in results:
                mold_sum=mold_sum+res['count']
        return jsonify({"tree_sum": tree_sum, "weed_sum": weed_sum,"mold_sum": mold_sum})
    except Exception as e:
        print(e)
        return jsonify({"ok": False, "error": str(e)})
    
@app.route("/fivedays")
def fivedays():
    try:
        with db.cursor() as cursor:
            for num_days in range(10):
              #print("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
                num_dist=cursor.execute("""select DISTINCT created_date from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW())""" % num_days)
                if num_dist==5:
                    break;

            cursor.execute("""select * from allergens WHERE created_date BETWEEN DATE(NOW() - INTERVAL %s DAY) AND DATE(NOW()) ORDER BY created_date""" %num_days)
            results=cursor.fetchall()
        return jsonify(results)
    except Exception as e:
        print(e)
        return jsonify({"ok": False, "error": str(e)})
