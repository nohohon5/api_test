#Test Fixtures即setUp（用例准备）及tearDown（测试清理）方法，用于分别在测试前及测试后执行
"""
setUp()/tearDown(): 每个用例执行前/后执行一次
setUpClass()/tearDownClass(): 每个测试类加载时/结束时执行一次
setUpMoudle()/tearDownMoudle(): 每个测试模块（一个py文件为一个模块）加载/结束时执行一次
"""

import unittest

def setUpMoudle():
    print("---setUpMoudle---")

def tearDownMoudle():
    print("---tearDownMoudle---")

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("---setupclass---")

    @classmethod
    def tearDownClass(cls):
        print("---teardownclass---")

    def setUp(self):
        print("--setup---")

    def tearDown(self):
        print("---teardown---")

    def test_a(self):  # 测试用例
        print("a")

    def test_B(self):  # 大写B的ascii比小写a靠前，会比test_a先执行
        print("B")




class TestClass2(unittest.TestCase):  # 该模块另一个测试类
    def test_A(self):
        print("A")

if __name__ == '__main__':
    unittest.main()