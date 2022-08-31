from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

eage = Edge()

eage.get('https://www.lagou.com/')
frame = eage.find_element(By.XPATH,'/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/p[1]/a')
frame.click()
time.sleep(1)

eage.find_element(By.XPATH,'/html/body/div[7]/div[1]/div[1]/div[1]/form/input[1]').send_keys('python',Keys.ENTER)
time.sleep(1)

list1 = eage.find_elements(By.XPATH,'/html/body/div/div[1]/div/div[2]/div[3]/div/div[1]/div')

for it in list1:
    name = it.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text
    price = it.find_element(By.XPATH,'./div[1]/div[1]/div[2]/span').text
    print(name,price)

'''在selenium中是不会自动切换页面的，所以在点击之后如果产生新页面之后需要手动输入指令切换'''
eage.find_element(By.XPATH,'/html/body/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
time.sleep(1)
#进行切换
eage.switch_to.window(eage.window_handles[-1]) #最后的一个窗口
job_detail = eage.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text
time.sleep(1)
print(job_detail)

eage.close() #关闭当前窗口
eage.switch_to.window(eage.window_handles[0]) #在切换回第一个页面
time.sleep(1)
company = eage.find_element(By.XPATH,'/html/body/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[2]/div[1]').text
time.sleep(1)
print(company)
'''selenium的xpath中最好用相对路径,绝对路径容易出问题，报错'''