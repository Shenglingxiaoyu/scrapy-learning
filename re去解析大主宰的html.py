import requests
import re

url = 'https://www.biquge.biz/0_32/'
main_url = 'https://www.biquge.biz'
response = requests.get(url)

obj = re.compile(r'<dt>《大主宰》正文</dt>.*?</dl>',re.S)
result = obj.findall(response.text)[0]
#print(result)

list = []
list1 = []

obj1 = re.compile(r'<dd><a href="(?P<href>.*?)">.*?</a></dd>',re.S)
hrefs = obj1.finditer(result)
for it in hrefs:
    href = it.group('href')
    child_href = main_url+href
    list.append(child_href)

#print(it.group('href'))
obj3 = re.compile(r'<a href="/">笔趣鸽</a> &gt; <a href="">玄幻小说</a> &gt; <a href="/0_32/">大主宰</a> &gt;(?P<name>.*?)\n</div>',re.S)
obj4 = re.compile(r'<div id="content">(?P<content>.*?)<div class="bottem2">',re.S)

for itt in list:
    child_response = requests.get(itt)
    child_response_text = child_response.text
    #print(child_response_text)
    name = obj3.search(child_response_text)
    content = obj4.search(child_response_text)
    final = content.group('content').replace('<br><br>　　','')

    print(name.group('name'))
    print(final)
