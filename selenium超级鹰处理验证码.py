from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chaojiying import Chaojiying_Client
import time

eage = Edge()

eage.get('https://www.chaojiying.com/user/login/')

eage.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('13802830346')
eage.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('Aocnsd1725361201')
img = eage.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png

#处理验证码
chaojiying = Chaojiying_Client('13802830346', 'Aocnsd1725361201', '938157')
dic = chaojiying.PostPic(img, 1902)
varify_code = dic['pic_str']

eage.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(varify_code)
time.sleep(5)
eage.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()