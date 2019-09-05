from db2 import DB

db = DB()  # 实例化一个数据库操作对象
if db.check_user("张三"):
    db.del_user("张三")