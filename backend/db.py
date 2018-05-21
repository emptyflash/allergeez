import pymysql
import os

def connect_db():
    host = os.environ.get("MYSQL_HOST", "localhost")
    port = os.environ.get("MYSQL_PORT", None)
    user = os.environ.get("MYSQL_USER", "root")
    pw = os.environ.get("MYSQL_PW", "")
    db = os.environ.get("MYSQL_DB", "db")
    return pymysql.connect(host=host,
                           port=port,
                           user=user,
                           password=pw,
                           db=db,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

if __name__ == "__main__":
    db = connect_db()
    try:
        with db.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS `allergens` (
              `allergen_id` int(11) PRIMARY KEY AUTO_INCREMENT,
              `allergen_type` varchar(255) DEFAULT NULL,
              `allergen_name` varchar(255) DEFAULT NULL,
              `count` int(11) DEFAULT NULL,
              `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='HACKATHON';""")
            db.commit()
            cursor.execute("""CREATE TABLE IF NOT EXISTS `users` (
              `id` int(11) PRIMARY KEY AUTO_INCREMENT,
              `endpoint` varchar(255) DEFAULT NULL,
              `auth` varchar(255) DEFAULT NULL,
              `p256dh` varchar(255) DEFAULT NULL,
              `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='HACKATHON';""")
            db.commit()
            cursor.execute("""CREATE TABLE IF NOT EXISTS `subscriptions` (
              `id` int(11) PRIMARY KEY AUTO_INCREMENT,
              `threshold` varchar(15) NOT NULL,
              `allergen_name` varchar(255) NOT NULL,
              `user_id` int(11) NOT NULL REFERENCES users(id)
            );""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS `feedback` (
              `id` int(11) PRIMARY KEY AUTO_INCREMENT,
              `emotion` varchar(255) DEFAULT NULL,
              `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
              `user_id` int(11) NOT NULL REFERENCES users(id)
            );""")
            db.commit()
    except Excetpion as e:
        print(e)
    finally:
        db.close()
