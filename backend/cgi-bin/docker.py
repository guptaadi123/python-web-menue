#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

name = mydata.getvalue("a")
hostvolume=mydata.getvalue("b")
t=mydata.getvalue("c")
hp=mydata.getvalue("d")
cp=mydata.getvalue("e")
image = mydata.getvalue("f")
#print(name)
#print(hostvolume)
#print(image)
#print(t)
cmd =  "sudo docker run -dit --name {0} -p {1}:{2} -v {3}:{4} {5}".format(name,hp,cp,hostvolume,t,image)
print(cmd)
o = subprocess.getoutput(cmd)
print(o)
