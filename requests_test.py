#请求方法
"""
requests.get()
requests.post()
requests.put()
...
requests.session(): 用于保持会话（session）
除了requests.session()外，其他请求方法的参数都差不多，都包含url，params, data, headers, cookies, files, auth, timeout等等
"""
#请求参数
"""url: 字符串格式，参数也可以直接写到url中
params：url参数，字典格式
data: 请求数据，字典或字符串格式
headers: 请求头，字典格式
cookies: 字典格式，可以通过携带cookies绕过登录
files: 字典格式，用于混合表单（form-data）中上传文件
auth: Basic Auth授权，数组格式 auth=(user,password)
timeout: 超时时间（防止请求一直没有响应，最长等待时间），数字格式，单位为秒
"""

import requests
import json

res = requests.get("https://www.baidu.com")
print(res.status_code, res.reason) # 200 OK
print(res.text) # 文本格式，有乱码
print(res.content) # 二进制格式
print(res.encoding) # 查看解码格式 ISO-8859-1
print(res.apparent_encoding) # utf-8
res.encoding='utf-8' # 手动设置解码格式为utf-8
print(res.text) # 乱码问题被解决
print(res.cookies.items()) # cookies中的所有的项 [('BDORZ', '27315')]
print(res.cookies.get("BDORZ")) # 获取cookies中BDORZ所对应的值 27315

s = requests.session()
s.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"username":"admin","password":"123456"}) # 发送登录请求
res = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs")
print(res.text)

#不使用保持会话的方式
requests.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"username":"admin","password":"123456"}) # 发送登录请求
res1 = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs")
print(res1.text)

#使用写cookie的方式
url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
cookies = {"PHPSESSID":"b064c37e6d73bbf087c1231b301a2f04"}
res = requests.get(url=url,cookies=cookies)
print(res.text)

app_key = 'kPoFYw85FXsnojsy5bB9hu6x'
secret_key = 'l7SuGBkDQHkjiTPU3m6NaNddD6SCvDMC'
img_url = 'http://upload-images.jianshu.io/upload_images/7575721-40c847532432e852.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
# 获取token
get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(app_key,secret_key)
token = requests.get(url=get_token_url).json().get("access_token")  # 从获取token接口的响应中取得token值
# 识别图片文字
orc_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}'.format(token)
data = {"url": img_url}
res = requests.post(url=orc_url, data=data)
print(json.dumps(res.json(), indent=2, ensure_ascii=False)) # 格式化输出

