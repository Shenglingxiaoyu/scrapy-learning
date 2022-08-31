import requests
from bs4 import BeautifulSoup
url = "http://www.xinfadi.com.cn/index.html"
response = requests.get(url)
response.close()

page = BeautifulSoup(response.text)
div = page.find("div",id="about")                 #先找标签，再找属性(因class是python关键字，所以可以在后面加_已示区别)
div1 = div.find_all("tr")[1:2]

for it in div1:
    print(it)
    div2 = it.find_all("th",width="140px")
    name = div2[0].text
    low = div2[1].text
    agv = div2[2].text
    high = div2[3].text
    rule = div2[4].text
    local = div2[5].text

print(name,low,agv,high,rule,local)