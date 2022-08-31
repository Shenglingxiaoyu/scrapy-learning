import requests
from lxml import etree

url = 'https://www.mcbbs.net/forum.php?mod=viewthread&tid=1310576&extra=page%3D1%26filter%3Dsortid%26sortid%3D3'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
           ' Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}
response = requests.get(url,headers=headers)

print(response.text)

result = etree.HTML(response.text).xpath('/html/body/div[7]/div[3]/div/div[2]/div[4]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/table/tbody/tr[1]/td')
print(result)