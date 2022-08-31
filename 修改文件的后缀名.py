import os

files = os.listdir('D:\pythonProject1\小说1')

for it in files:
    newname = it+'.txt'
    os.chdir('D:\pythonProject1\小说1')
    os.rename(it,newname)