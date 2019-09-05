import requests
import json
api_url = 'http://www.tuling123.com/openapi/api'
while 1:
    text_input = input("me:")
    data = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        },
        "inputImage": {
            "url": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1564052831426&di=1d3a2ab60eb497fce6ae7fcc677cf2fe&imgtype=0&src=http%3A%2F%2Fimg.alicdn.com%2Fimgextra%2Fi1%2FTB20TZftb1YBuNjSszeXXablFXa_%2521%25212144992932.jpg_400x400.jpg"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "北京",
                "street": "信息路"
            }
        },
        "inputText": {
            "Text": text_input
        },
    },
    "userInfo": {
         "apiKey": "ec961279f453459b9248f0aeb6600bbe",
          "userId": "206379"
    }
}
    data = json.dumps(data).encode('utf8')
    response_str = requests.post(api_url, data=data, headers={'content-type': 'application/json'})
    #response_dic = response_str.json()
    # print('返回结果：' + response_str.text)
    #results_text = response_dic['results'][0]['values']['text']
    print(response_str.json())
