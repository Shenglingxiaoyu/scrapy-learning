import requests
url = 'https://cn.bing.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'}

response = requests.get(url,headers = headers)
print(response)
print(response.text)
response.close()