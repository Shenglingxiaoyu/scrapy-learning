import requests
import re
url = "https://movie.douban.com/chart"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}

response = requests.get(url,headers=headers)
page_content = response.text


obj = re.compile(r'</td>.*?<td valign="top">.*?class="">(?P<name>.*?)/ <span style="font-size:13px;">.*?<span class="rating_nums">(?P<score>.*?)</span>.*?'
                 r'<span class="pl">\((?P<num>.*?)人评价\)',re.S)

result = obj.finditer(page_content)
for it in result:
    print(it.group('name'))
    print(it.group('score'))
    print(it.group('num'))

response.close()


#有待测试