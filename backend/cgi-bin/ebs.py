#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi
name= "date"
form = cgi.FieldStorage()
vtype = form.getvalue("vtype")
region = form.getvalue("region")
access_key = form.getvalue("akey")
secret_key = form.getvalue("skey")
size = form.getvalue("size")
AZ = form.getvalue("AZ")
cmd="AWS_ACCESS_KEY_ID={0} AWS_SECRET_ACCESS_KEY={1} aws ec2 create-volume --volume-type {2} --size {3} --availability-zone  {4}   --region {5} --output text".format(access_key,secret_key,vtype,size,AZ,region)
output = sp.getstatusoutput(cmd)
if output[0]==0:
 
 print(output[1])

else:
  print("Some Error Occured Please Contact Admin")

