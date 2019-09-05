import pymysql

def get_db_conn():
    conn = pymysql.connect(
        host="192.168.100.78",
        port=3306,
        user="root",
        passwd="root",
        db="51fanli_zymall",
        charset='utf8'
    )
    return conn

#查询sql
def query_sql(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


#更改数据操作
def change_sql(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def check_zc(activity_id):
    sql = "SELECT * FROM seller_coupon where activity_id= '{}'".format(activity_id)
    result = query_sql(sql)
    return True if result else False

def add_user(name, password):
    sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
    result = change_sql(sql)

def del_zc(activity_id):
    sql = "SELECT * FROM seller_coupon where activity_id= '{}'".format(activity_id)
    change_sql(sql)