#coding=utf-8
# 功能: 爬取喜马拉雅
# 创建者：俺
import re
import requests
url="https://www.ximalaya.com/album/6233693"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'} # 模拟浏览器
response=requests.get(url=url, headers=headers)
audia_info=re.findall('"trackId":(\d+),"isPaid":false,"tag":0,"title":"(.*?)","playCount"', response.text)
for id,title in audia_info:
    link = 'https://www.ximalaya.com/revision/play/v1/audio?id='+id+'&ptype=1'
    audia_content = requests.get(url=link, headers=headers)
    audia_url = audia_content.json()['data']['src'] # 播放地址
    audio = requests.get(url=audia_url,headers=headers).content
    with open(title + '.mp3' , 'wb') as f:
        f.write(audio)
    print(f"正在下载{title}")
print(f"下载完成")