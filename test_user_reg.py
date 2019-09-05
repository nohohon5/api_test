"""
接口测试用例：
数据准备：准备测试数据，可手工准备，也可使用代码准备（通常涉及数据库操作）
环境检查：如果手工准备的数据，连接数据库进行环境检查会使用例更健壮
发送请求：发送接口请求
响应断言/数据库断言：响应断言后，还需要进行数据库断言，以确保接口数据库操作的正确性
数据清理：如果接口有更数据库操作，断言结束后需要还原更改
"""
import unittest
import requests
import json
from db import *

# 数据准备
Not_Exit_User = '1111'
Exit_User = '213'


class TestZcCoupon(unittest.TestCase):
    url = 'https://pb.shzyfl.cn/h5/store/ajaxGetZcCoupons'

    def test_coupon_not_exit(self):
        # 环境检查
        if not check_zc(Not_Exit_User):
            print("无数据")

        # 发送请求
        data = {"zc_id": Not_Exit_User}
        res = requests.post(url=self.url, json=data, verify=False)

        ## 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        excp_res = {
            "status": 1,
            "info": "请配置后台优惠券",
            "data": {
                "coupons": [

                ]
            }
        }

        # 响应断言
        self.assertDictEqual(res.json(), excp_res)


    def test_coupon_exit(self):
        if check_zc(Exit_User):
            print("有数据")

        # 发送请求
        data_json = {"zc_id": 213}
        res = requests.get(url=self.url, data=data_json, verify=False)
        print(res.text)

        except_res = {
            "status": 1,
            "info": "success",
            "data": {
                "coupons": [
                    {
                        "id": "4013",
                        "coupon_price": 1,
                        "discount_price": 10,
                        "coupon_status": "1",
                        "state": 1
                    }
                ]
            }
        }
        # 响应断言（整体断言）
        self.assertDictEqual(res.json(), except_res)

#    if __name__ == '__main__':
#   unittest.main(verbosity=2)  # 运行所有用例
