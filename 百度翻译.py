import requests
url = 'https://fanyi.baidu.com/sug'
variable = input('请输入翻译内容')
dat = {"kw": variable}
response = requests.post(url,date=dat)
print(response)
response.close()