import requests

url = 'https://www.bilibili.com/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
           ' Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'}
response = requests.get(url,headers=headers)
print(response.text)