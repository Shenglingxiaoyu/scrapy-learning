import requests
from lxml import etree
from bs4 import BeautifulSoup


main_url = 'https://pic.netbian.com'
url = 'https://pic.netbian.com/4kdongman/'

response = requests.get(url)
response.encoding = 'gbk'
response.close()


html = etree.HTML(response.text)
lis = html.xpath('/html/body/div[2]/div/div[3]/ul/li')

list1 = []
list2 = []

for it in lis:
    href = it.xpath('./a/@href')[0]
    child_hrefs = main_url+href
    #print(child_hrefs)
    list1.append(child_hrefs)

    #print(href)

for itt in list1:

    child_response = requests.get(itt)
    child_response.encoding = 'gbk'

    child_html = BeautifulSoup(child_response.text,'html.parser')
    pic = child_html.find('div',class_="photo-pic")

    img = pic.find('img')
    #print(img)
    src = img.get('src')
    child_img = main_url+src
    list2.append(child_img)


for ittt in list2:
    print(ittt)
    img_response = requests.get(ittt)

    picture_name = ittt.split('/')[-1]


    #print(picture_name)
    with open('jpg/'+picture_name,'wb') as file:
        file.write(img_response.content)

    print('over',picture_name)







