import unittest
from test_user_reg import TestZcCoupon

suite = unittest.TestSuite
def testcouponcase(self):
    self.test_coupon_not_exit()
    self.test_coupon_exit()

suite.addTest(testcouponcase())
#testcases = [TestZcCoupon('test_coupon_not_exit'),TestZcCoupon('test_coupon_exit')]
#suite.addTests(self=suite,tests=testcases)

# 运行测试集
unittest.TextTestRunner(verbosity=2).run(suite)  # verbosity显示级别，运行顺序为添加到suite中的顺序
