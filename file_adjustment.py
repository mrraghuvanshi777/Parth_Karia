import os
import shutil
path=os.getcwd()
files=[]
n=str(input('enter folder name :'))
new=os.path.join(path,n)
os.mkdir(new)
os.chdir(new)
t=str(input('enter which type of file u want to enter in new folder:'))
files=os.listdir(path)
for i in range(0,len(files)):
    name,ex=os.path.splitext(files[i])
    if ex==t:
        path1=os.path.join(path,files[i])
        shutil.move(path1,os.getcwd())
       
       
        