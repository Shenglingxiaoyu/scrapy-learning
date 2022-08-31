from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

eage = Edge()
eage.get('http://m.qiukwi.com/play/shicaolaolongbeiguanyielongzhiming-1-5.html')

iframe = eage.find_element(By.XPATH,'//*[@id="playleft"]/iframe')
'''因为很多网页的iframe并不在源代码里面，是通过scrpit获得iframe，但是可以在元素里面获取，因为元素就是页面最后加载的结果'''
eage.switch_to.frame(iframe) #需要跳转到iframe页面
player = eage.find_element(By.XPATH,'./document/html/head/title').text #在iframe里面找东西
print(player)
eage.switch_to.default_content() #回到默认界面，比如切换到iframe，然后再切换原来的页面
