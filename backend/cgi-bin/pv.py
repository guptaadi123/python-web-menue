#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp
import os

form = cgi.FieldStorage()

# To get the input from the user
diskList = form.getvalue("diskList")

# To remove the comma and convert diskList into List
diskList = diskList.split(',')
#print(diskList)
for f in diskList:
 cmd=("sudo pvcreate disk {}".format(f))
 outpv = sp.getstatusoutput(cmd)
 print(outpv)
 if outpv[0]==0:
  print("pv created")
  

