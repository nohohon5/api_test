import unittest
from test_user_reg import TestZcCoupon

suite2 = unittest.makeSuite(TestZcCoupon)
unittest.TextTestRunner(verbosity=2).run(suite2)