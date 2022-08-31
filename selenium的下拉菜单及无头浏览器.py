import time
from selenium.webdriver import Edge                  #导入浏览器
from selenium.webdriver.support.select import Select    #将下拉列表封装成下拉菜单
from selenium.webdriver.common.by import By             #find_element通过by哪个要素去寻找
from selenium.webdriver.edge.options import Options      #浏览器的设置信息

option = Options()
option.add_argument('--headless')
option.add_argument('--disable-gpu')

eage = Edge(options=option)
eage.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

'''找到下拉列表'''
select = eage.find_element(By.XPATH,'//*[@id="OptionDate"]')
'''将下拉列表封装成下拉菜单'''
select_m = Select(select)

for it in range(len(select_m.options)):   #options为选项，列表的选项,此时it为下拉菜单的索引位置
    select_m.select_by_index(it)     #按照索引进行自动切换，不需要用switch_to
    time.sleep(2)
    table = eage.find_element(By.XPATH,'//*[@id="TableList"]/table').text
    with open('票房信息/'+str(it),'w') as file:
        file.write(table)


'''获得页面的代码，并非源代码，此代码是经过加载，js加载等等得到的代码，也就是element里的东西'''
'''print(eage.page_source)'''