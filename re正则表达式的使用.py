import re
#findall:匹配字符串中所有符合正则的内容，返回对象为数组
list = re.findall(r'\d+','我的QQ号是：2904523991')                                    #正则表达式，字符串
print(list)            #注意在findall的情况下，不能用group

#finditer：匹配字符串中的所有内容，返回的是迭代器，饱含了多个match对象
#其中的string（字符串），可以用包含了返回html的变量中
'''finditer的好处就是可以自由选定你想要的信息
如果是findall的话则会返回所有信息'''                            #match匹配


it = re.finditer(r'\d+','我的QQ号是：2904523991')                 #正则表示式前面加r的意义是为了使反斜杠不使后面的字符转义，表达原来的意思
for match in it:
    print(match.group())              #group的作用是取组


#search:返回的是match对象，唯一一个数据，拿数据需要group（也是全文匹配）  ,返回只有一个match数据
search = re.search(r'\d+','我的QQ号是2904523991')
print(search.group())


m = re.match(r'\d+','2904523991')                 #re.match从头开始匹配
print(m.group())


#正则表达式的预加载
obj = re.compile(r'\d+')
response = obj.finditer('你好，在吗，我的QQ号是2904523991')
for i in response:
    print(i.group())


s = '''
<div class='jay'><span id='1'>过期了</span></div>
<div class='sjkdbt'><span id='2'>ghj</span></div>
<div class='skjdgt'><span id='3'>sdfgh</span></div>
<div class='sdkjbtt'><span id='4'>askegrh</span></div>
<div class='jasdkjgt'><span id='5'>sadkgt</span></div>
'''
qqq = re.compile(r"<div class='.*?'><span id='(?P<no>\d)+'>(?P<yes>.*?)</span></div>",re.S)       #re.S的作用是让.能匹配到换行符

'''正则表达式的前后加的括号，括号里的表达式之前加个"?P<>"
（尖叫括号里面输入想要给表达式赋予的命名）
'''

response1 = qqq.finditer(s)
for ma in response1:
    print(ma.group("no"))           #要注意，如果group制定组，括号里面要加引号
    print(ma.group("yes"))



'''finall不能用.group,而finditer/search/march都可以用.group'''




