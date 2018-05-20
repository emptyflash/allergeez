from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

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
            user_sql = "INSERT INTO `users` (`endpoint`) VALUES (%s)"
            cursor.execute(user_sql, [data["endpoint"]])
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


