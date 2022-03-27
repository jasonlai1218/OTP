import pymysql


def get_password_from_db(account):
    try:
        conn = pymysql.Connect(host='127.0.0.1', user='root', password='xxx', db='mysql')
        cur = conn.cursor()
        cur.execute("SELECT Password FROM user WHERE account = %s" % account)
        for r in cur:
            return r
    finally:
        cur.close()
        conn.close()
