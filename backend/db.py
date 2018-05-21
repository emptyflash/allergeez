import pymysql
import os

def connect_db():
    host = os.environ.get("MYSQL_HOST", "localhost")
    port = os.environ.get("MYSQL_PORT", 0)
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
