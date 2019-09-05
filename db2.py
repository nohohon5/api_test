"""
封装：
        在python中，封装按照如下步骤进行操作
        (1) 定义类型，所有属性私有化[双下划线开头]
        (2) 每个属性提供set/get方法[赋值/取值]
            命名规范：赋值：set_属性名称(..)
                    取值：get_属性名称(..)
        (3) 在get/set方法中，提供限制条件！
"""

import pymysql

class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host="192.168.100.78",
            port=3306,
            user="root",
            passwd="root",
            db="51fanli_zymall",
            charset='utf8'
        )
        self.cur = self.conn.cursor()

#在对象删除时触发__del__(self),然后再删除对象自己。如果对象没有删除，程序结束时，会自动删除对象

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self, name):
        result = self.query("select * from user where name='{}'".format(name))
        return True if result else False

    def del_user(self, name):
        self.exec("delete from user where name='{}'".format(name))




