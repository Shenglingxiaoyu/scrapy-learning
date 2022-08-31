import requests
import asyncio
import aiohttp
import aiofiles
from lxml import etree
from bs4 import BeautifulSoup

main_url = 'https://b.faloo.com'
url = 'https://b.faloo.com/html_1171_1171645/'

response = requests.get(url)
html = etree.HTML(response.text)

list1 = html.xpath('/html/body/div[2]/div[3]/div[4]/div[3]/a/@href')

list1 = [main_url+it for it in list1]
print(list1)

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.text(encoding='gb18030')
            html = etree.HTML(response_text)
            title = html.xpath('//*[@id="center"]/div/div[1]/h1/text()')
            content = html.xpath('/html/body/div[6]/div/div[5]/text()')
            print(title)
            async with aiofiles.open('小说1/'+str(title),'w') as file:
                await file.write(f'{title}\n'+f'\t{content}')

async def main():
    tasks = []


    task = download('https://b.faloo.com//b.faloo.com/1171645_1.html')
    task_object = asyncio.create_task(task)
    tasks.append(task_object)

    await asyncio.wait(tasks)

if __name__ == '__main__':

    asyncio.get_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy)
    asyncio.run(main())