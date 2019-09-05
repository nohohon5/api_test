import json
import requests
#序列化（字典 -> 文本/文件句柄）： json.dumps()/json.dump()
#反序列化（文本/文件句柄 -> 字典) : json.loads()/json.load()

data = {
    "name":"zhangsan",
    "male":True,
    "money": None,
}
res = json.dumps(data) #序列化，转化为合法的JSON文本（方便HTTP传输）
print(res)


#反序列化
res_text = {"name": "\u5f20\u4e09", "password": "123456", "male": True, "money": None}  # JSON文本格式的响应信息
res_dict = json.loads(res_text) # 转化为字典
print(res_dict['name'])  # 方便获取其中的参数值


res2 = requests.post("http://10.0.5.103:8184/recom/9k9/recom9k9Item?uid=8427998&page=1&pageSize=20&9k9cateid=all&group=46901e",verify=False)
print(res2.text)
#res2.decode("UTF-8")
#res_dict = json.loads(res2)
print(json.dumps(json.loads(res2), indent=2, sort_keys=True, ensure_ascii=False))
#indent: 缩进空格数，indent=0输出为一行
#sork_keys=True: 将json结果的key按ascii码排序
#ensure_ascii=Fasle: 不确保ascii码，如果返回格式为utf-8包含中文，不转化为\u..


#反序列化
res_text = {"name": "\u5f20\u4e09", "password": "123456", "male": true, "money": null}  # JSON文本格式的响应信息
res_dict = json.loads(res_text) # 转化为字典
print(res_dict['name'])  # 方便获取其中的参数值

# method支持get和post，如果没有method，有data默认发post请求，没有data默认发get请求，type支持：form或json，没有默认发form格式
{
  "url": "http://www.tuling123.com/openapi/api",
  "method": "get",
  "params": {
    "key": "ec961279f453459b9248f0aeb6600bbe",
    "info": "你好"
  }
}

{
  "url": "http://openapi.tuling123.com/openapi/api/v2",
  "method": "post",
  "type": "json",
  "data": {
    "reqType": 0,
    "perception": {
      "inputText": {
        "text": "附近的酒店"
      },
      "inputImage": {
        "url": "imageUrl"
      },
      "selfInfo": {
        "location": {
          "city": "北京",
          "province": "北京",
          "street": "信息路"
        }
      }
    },
    "userInfo": {
      "apiKey": "ec961279f453459b9248f0aeb6600bbe",
      "userId": "206379"
    }
  }
}