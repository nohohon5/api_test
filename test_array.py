import unittest
from test_user_reg import TestZcCoupon
from HTMLTestReportCN import HTMLTestRunner

suite1 = unittest.TestSuite()
suite1.addTest(TestZcCoupon('test_coupon_not_exit'))

suite2 = unittest.makeSuite(TestZcCoupon,'test_coupon_exit')

suite = unittest.TestSuite([suite1, suite2])  # 将两个测试集组合为一个

unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.defaultTestLoader.discover("./")  # 遍历当前目录及子包中所有test_*.py中所有unittest用例
#
# # 输出测试结果到文本文件 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件；'a' 对应的表示追加等
# with open("result.txt","w") as f:
#     unittest.TextTestRunner(stream=f,verbosity=2).run(suite) # 将输出流stream输出到文件

f = open("111report.html", 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="Api Test",description="测试描述").run(suite)

f.close()