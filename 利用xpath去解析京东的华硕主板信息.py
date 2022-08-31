import requests
from lxml import etree

url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E7%A1%95%E4%B8%BB%E6%9D%BF&enc=utf-8&wq=%E' \
      '5%8D%8E%E7%A1%95%E4%B8%BB%E6%9D%BF&pvid=c1fd5cdb124a472abdad653c35684872'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}

main_page = requests.get(url,headers= headers)
main_page.close()
#print(main_page.text)

html = etree.HTML(main_page.text)
lis = html.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li')

#print(lis)
for it in lis:
    price = it.xpath('./div/div[2]/strong/i/text()')
    name = it.xpath('./div/div[3]/a/em/text()')
    print(price,name)