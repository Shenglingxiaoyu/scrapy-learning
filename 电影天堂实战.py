import requests
import re
url = 'https://www.dygod.net/'
response = requests.get(url,verify=False)              #请求1
response.encoding = 'gb2312'
response.close()

obj1 = re.compile(r'华语电视剧.*?<ul>(?P<one>.*?)</ul>',re.S)
result = obj1.finditer(response.text)

child_href_list = []

for it in result:
    ul = it.group('one')
    obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
    result1 = obj2.finditer(ul)

    for itt in result1:
        href1 = itt.group('href')
        child_href = url+href1.strip('/')
        print(child_href)
        child_href_list.append(child_href)

        for ittt in child_href_list:
            header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                            ' Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}

            child_href_response = requests.get(ittt,headers=header)               #请求2
            child_href_response.encoding = 'gb2312'
            child_href_response.close()

            obj3 = re.compile(r'<td colspan="2" align="center" valign="top"><div id="Zoom">.*?◎片　　名　(?P<name>.*?)<br />'
                  r'.*?<ul>.*?<li><a href="'
                  r'(?P<download>.*?)">',re.S)

            result2 = obj3.finditer(child_href_response.text)
            for itttt in result2:
                print(itttt.group('name'))
                print(itttt.group('download'))






