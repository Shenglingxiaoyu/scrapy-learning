'''selenium的作用就是用程序来连接在浏览器，让浏览器帮我们完成复杂的操作，我们只接受结果'''
'''自动化测试工具'''
'''环境搭建
    1.pip install selenium
    2.下载浏览器驱动，每个浏览器驱动都不一样，还要对好浏览器的版本
    3.在下载好的浏览器驱动放在python解释器文件夹里'''
'''让selenium启动浏览器，先导入'''
from selenium.webdriver import Edge

'''1.创建浏览器对象'''
eage = Edge()

'''2.打开网页'''
eage.get('http://www.baidu.com')
print(eage.title)