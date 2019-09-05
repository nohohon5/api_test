import pymysql
#1.建立连接
conn = pymysql.connect(
    host="192.168.100.78",
    port=3306,
    user="root",
    passwd="root",
    db="51fanli_zymall",
    charset='utf8'
)
#2.建立游标
cur = conn.cursor()
#3.查询数据库
cur.execute("SELECT *  FROM product WHERE SELLER_ID=41")
#4.获取查询结果
result = cur.fetchall()
print(result)

#3.更新数据
cur.execute("UPDATE product SET brand_id=2 WHERE product_code=88880000000173")
#4.提交修改
conn.commit()  # 注意是用的conn不是cur


#5.关闭游标和连接
cur.close()
conn.close()



#回滚数据
try:
    cur.execute("DELETE FROM product WHERE product_code=88880000000173")
    conn.commit()
except Exception as e:
    conn.rollback()
    print(str(e))