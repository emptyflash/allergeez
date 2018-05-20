import pymysql

db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with db.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS `allergens` (
          `allergen_id` int(11) PRIMARY KEY AUTO_INCREMENT,
          `allergen_type` varchar(255) DEFAULT NULL,
          `allergen_name` varchar(255) DEFAULT NULL,
          `count` int(11) DEFAULT NULL,
          `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
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
        db.commit()
finally:
    db.close()
