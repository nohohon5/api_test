import requests
import json

#发送请求获取响应 绕过SSL验证
res = requests.get("https://pb.shzyfl.cn/h5/store", verify=False)
#输出响应
print(res.text)


#带参数的get请求
res1 = requests.get("https://pb.shzyfl.cn/h5/store/ajaxGetZcCoupons?zc_id=211", verify=False)
print(res1.text)

#提交表单post请求
url = 'https://pb.shzyfl.cn/h5/store/ajaxGetLimitItems'
params = {"zc_id":"207","pid":"88880001005401"}   #将参数放入字典格式中
res2 = requests.get(url=url,params=params,verify=False)
print("res2的结果：")
print(res2.text)

#json格式post请求
url = 'http://httpbin.org/post'
data = '{"name": "hanzhichao", "age": 18}'  #多行文本, 字符串格式，也可以单行（注意外层有引号，为字符串）
res3 = requests.post(url=url,data=data,verify=False) #data支持字典和字符串
print("res3的结果：")
print(res3.text)

#一般来说，建议将data声明为字典格式（方便数据添加修改），然后再用json.dumps()方法把data转换为合法的JSON字符串格式
url = "http://httpbin.org/post"
data = {
        "name": "hanzhichao",
        "age": 18
        }  # 字典格式，方便添加
headers = {"Content-Type":"application/json"} # 严格来说，我们需要在请求头里声明我们发送的格式
res4 = requests.post(url=url, data=json.dumps(data), headers=headers) #  将字典格式的data变量转换为合法的JSON字符串传给post的data参数
print("res4的结果：")
print(res4.text)


#或直接将字典格式的data数据赋给post方法的JSON参数（会自动将字典格式转为合法的JSON文本并添加headers）

url = "http://httpbin.org/post"
data = {
        "name": "hanzhichao",
        "age": 18
        }  # 字典格式，方便添加
res5 = requests.post(url=url,json=data)
print("res5的结果：")
print(res5.text)