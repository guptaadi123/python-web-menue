#!/usr/bin/python3
print("content-type:text/html")
print()
import cgi
import subprocess as sp
import os
form = cgi.FieldStorage()
# To get the input from the user
diskList = form.getvalue("diskList")
vgName = form.getvalue("vgName")
lvName = form.getvalue("lvName")
size = form.getvalue("size")
# To remove the comma and convert diskList into List
diskList = " ".join(diskList.split(','))
#print(diskList)
cmd="sudo vgcreate {0} {1}".format(vgName,diskList)
outvg = sp.getstatusoutput(cmd)
if outvg[0]==0:
 print("vg created")
 c= "sudo lvcreate --name {0}  --size {1} {2}".format(lvName,size,vgName)
 outlv = sp.getstatusoutput(c)
 if outlv[0]==0:
   print("lv created")

