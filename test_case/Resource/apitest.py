import requests
import json


url = "https://gateway.open.hand-china.com/hsmgt/v1/3/corallium-headers/page?page=0&size=12&type=TEMPLATE&shareFlag=true&categoryCode=&name="
# # r = requests.get(url).json()
# # print(r)
#
# res = requests.get(url) # res即返回的响应对象
# # 3. 解析响应
# print(res.text)  # 输出响应的文本

header={
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'authorization': 'bearer 847faa53-ea9b-497d-ac55-fdbb941070e5',
'sw8': '1-NDBlZWY0MTMtODk3ZS00YzlhLTlkM2ItMzgxMGFmZjdjMjM3-YjlkY2RlNDQtZWRkYS00YzY1LWExOWQtYjE3NDIzNDQ5MWQ2-0-S0lOR05FVy1QUk9EPGJyb3dzZXI+-MS4wLjA=-W2luZGV4XQ==-Z2F0ZXdheS5vcGVuLmhhbmQtY2hpbmEuY29t',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

result = requests.get(url=url,headers=header)
# print(result.text)
j = json.loads(result.text)
print(j)
print(j['totalElements'])

