import os
import subprocess
os.chdir("C:/Users/scien/Aria2/trackerslist")
subprocess.run(["git","pull"])
Din = open("trackers_all_http.txt","r")
data = Din.read()
data=data.replace('\n',',')
data=data.replace(",,",",")
Din.close
Din = open("blacklist.txt","r")
data2 = Din.read()
data2=data2.replace('\n',',')
data2=data2.replace(",,",",")
os.chdir("C:/Users/scien/Aria2")
conf=open("aria2.txt","r",-1,"UTF-8")
confi=conf.read()
data = confi.replace("@@@",data)
data = data.replace("###",data2)
Dout = open("aria2.conf","w",-1,"UTF-8")
Dout.write(data)
Dout.close
exit()
