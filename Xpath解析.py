import requests
from lxml import etree

url = 'https://passport.17k.com/login/'

postdata = {'username':'13802830346',
            'password':'Aocnsd1725361201'}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 '
                         'Safari/537.36 Edg/103.0.1264.71'}

session = requests.session()
response = session.post(url,data=postdata,headers=headers)
response.encoding = 'utf-8'
response.close
print(response.text)

