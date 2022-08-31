import requests
import aiohttp
import aiofiles
import asyncio
from lxml import etree
from bs4 import BeautifulSoup

main_url = 'https://fanqienovel.com'
url = 'https://fanqienovel.com/page/6982529841564224526?enter_from=stack-room'
response = requests.get(url)

page = BeautifulSoup(response.text,'html.parser')
aas = page.find_all('div',class_="chapter-item")
list1 = []

for it in aas:
    a = it.find('a').get('href')
    child_url = main_url+a
    list1.append(child_url)

async def download(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.text()

            child_page = BeautifulSoup(response_text,'html.parser')
            title = child_page.find('h1',class_="muye-reader-title").text
            content = child_page.find_all('p')

            content = [str(itt) for itt in content]
            content = ''.join(content).replace('<p>','').replace('</p>','')

            async with aiofiles.open('小说1/'+title,'w') as file:
                await file.write(f'{title}\n'+f'\t{content}')

async def main():
    tasks = []

    for itt in list1:
        task = download(itt)
        task_object = asyncio.create_task(task)
        tasks.append(task_object)

    await asyncio.wait(tasks)

if __name__ == '__main__':

    #asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
'''成功，代码是正确的，11章后面字少是因为网页那边的问题，网站那边需要付费或下载软件等等问题'''
