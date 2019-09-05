import unittest
import requests

class TestUserLogin(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类
    url = 'http://115.28.108.130:5000/api/user/login/'
    def test_user_login_normal(self):         #一条test必须以test开头
        data = {"user":"张三","password":"123456"}
        res = requests.post(url=self.url,data=data)
        self.assertIn("登陆成功",res.text)  #断言


    def test_user_login_fail(self):
        data = {"user":"张三","password":"1234564"}
        res = requests.post(url=self.url,data=data)
        self.assertIn("登陆失败",res.text)

if __name__ == '__main__':    #如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)   #运行本测试类所有用例,verbosity为结果显示级别

 #用例执行顺序：并非按书写顺序执行，而是按用例名ascii码先后顺序执行


case = unittest.TestCase()
case.assertEqual(1,2.0/2)
case.assertEqual(1, True) # 通过
case.assertIs(1.0, 2.0/2) # 失败，不是同一对象
case.assertListEqual([1,2],[1,2]) # 通过（顺序要一致）
case.assertDictEqual({"a":1,"b":2},{"b":2,"a":1}) # 通过，字典本无序
case.assertIsNone({}) # 失败
case.assertFalse({}) # 通过，空字典为False
case.assertIn("h","hello") # 通过
case.assertGreater(3,2) # 通过，3>2
case.assertIsInstance({"a":1}, dict) # 通过
