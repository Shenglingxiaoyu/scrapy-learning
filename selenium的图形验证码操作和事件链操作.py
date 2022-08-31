from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chaojiying import Chaojiying_Client
import time
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains      #事件链，已一套设定好的流程执行，最后一定要加.perform

option = Options()
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])


chaojiying = Chaojiying_Client('13802830346', 'Aocnsd1725361201', '938157')
edge = Edge(options=option)
edge.get('https://beta.mcbbs.net/login')

edge.find_element(By.XPATH,'//*[@id="el-id-8955-21"]').send_keys('2904523991@qq.com')

edge.find_element(By.XPATH,'//*[@id="el-id-8955-22"]').send_keys('Aocnsd1725361201')


edge.find_element(By.XPATH,'//*[@id="app"]/section/main/div[2]/div/div[3]/button').click()
time.sleep(5)

img = edge.find_element(By.XPATH,'/html/body/div[8]/div[2]/div[6]/div/div').screenshot_as_png
dic = chaojiying.PostPic(img, 9501)
result = dic['pic_str']
print(result)
