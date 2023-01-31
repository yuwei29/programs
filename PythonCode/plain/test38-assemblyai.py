import requests as rq
import time 
endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    # "audio_url": "https://bit.ly/3yxKEIY"
    'audio_url': 'https://cdn.jsdelivr.net/gh/blacktunes/hiiro-button@master/public/voices/I%20love%20you%20more%20than%20you%20love%20me.mp3' #'http://1.15.226.74:82/sci.mp3' #
}
headers = {
    "authorization": "f1ce5f0031724afd936a4bd0e8d3d830",
}
response = rq.post(endpoint, json=json, headers=headers)
resultId = response.json()['id']
print(resultId)
endpoint += '/'+resultId
print(endpoint)
# print(headers)
time.sleep(10) #从解析音频到生成文字需要一定的时间，2秒似乎不够，10秒在这个例子中可用
print(rq.get(endpoint,headers=headers).json()['text'])