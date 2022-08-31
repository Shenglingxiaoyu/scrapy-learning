import asyncio
import aiohttp         #这是一个异步请求网页的语句，就像requests

urls = ['https://pic.netbian.com/uploads/allimg/220726/002046-165876604635fe.jpg',
        'https://pic.netbian.com/uploads/allimg/190726/230851-15641537312b86.jpg',
        'https://pic.netbian.com/uploads/allimg/220814/224505-1660488305ba5e.jpg']

async def download(url):
    name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:        #async的意义是证明这一段语句是可以进行异步调度的
        async with session.get(url) as response:      #这里就相当于response = requests.get(url),这里是请求，所以会有阻塞

            with open('img/'+name,'wb') as file:
                file.write(await response.content.read())

    print(name,'over')

async def main():

    task = []
    for it in urls:
        task.append(asyncio.create_task(download(it)))

    await asyncio.wait(task)    #asyncio.wait是等待所有任务收集完成，然后再run函数里面执行，await的作用是挂起，等待有阻塞发生

asyncio.run(main())

'''async的意义是当协程对象遇到阻塞的时候，将协程对象切出去，相当于切到一个新的线程里，在这个线程里执行挂起任务(就是await)，挂起任务在实际上
就是暂停工作(相当于休息，但这个休息也是一个任务，它要执行这个休息任务)，在结束挂起任务之后在切回主线程继续执行原先要进行的任务'''

