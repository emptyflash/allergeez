
from bs4 import BeautifulSoup
import requests
from datetime import datetime

import pymysql

db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS `allergens` (
  `allergen_id` int(11) PRIMARY KEY AUTO_INCREMENT,
  `allergen_type` varchar(255) DEFAULT NULL,
  `allergen_name` varchar(255) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='HACKATHON';""")

db.commit()

#cursor.execute("""select * from allergens""")
#print(cursor.fetchall())


#cursor = db.cursor()
#cursor.execute("""DROP TABLE `allergens`;""")


#db.commit()

db.close()
