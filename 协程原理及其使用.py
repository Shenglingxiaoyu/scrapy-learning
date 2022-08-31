'''协程是比线程更轻量级的存在，对于cpu来说它就是一个单线程，在一条线程里面，如果有任务遇到阻塞状态(IO操作)便会切换到其他任务执行，
等到阻塞状态结束，在返回在前面的任务继续执行，这就叫做异步协程'''
import time
import asyncio
#
# async def fun():         #此函数为异步协程函数，是不能直接调用fun()函数进行使用
#     print('你好，我叫小宇')
#
# g = fun()
# print(g)
# asyncio.run(fun())       #异步协程函数的调用
'''在对象前面写async的目的是声名这个函数是异步协程，这样才可以进行协程调用，不写就默认是同步操作'''
'''协程需要有多个协程对象在同一条线程里面运行'''

async def fun1():
    print('你好，我叫小宇')
    await asyncio.sleep(3)     #await的作用是将此程序挂起，让后面的程序顶上来运行(因为遇到阻塞所以需要手动将此程序挂起)
    print('你好，我叫小宇')

async def fun2():
    print('你好，我叫小毅')
    await asyncio.sleep(2)
    print('你好，我叫小毅')

async def fun3():
    print('你好，我叫emmm')
    await asyncio.sleep(4)
    print('你好，我叫emmm')


async def main():         #这个地方就相当于将所有任务都封装在一起
    task = [asyncio.create_task(fun1()),
            asyncio.create_task(fun2()),
            asyncio.create_task(fun3())
            ]
    await asyncio.wait(task)


t1 = time.time()
asyncio.run(main())
t2 = time.time()
print(t2-t1)






