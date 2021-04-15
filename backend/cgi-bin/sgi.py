#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi
name= "date"
form = cgi.FieldStorage()
sg_name = form.getvalue("sg_name")
region = form.getvalue("region")
access_key = form.getvalue("akey")
secret_key = form.getvalue("skey")
cmd="AWS_ACCESS_KEY_ID={0} AWS_SECRET_ACCESS_KEY={1} aws ec2 describe-security-groups --group-names {2}   --region {3}   --output text ".format(access_key,secret_key,sg_name,region)
output = sp.getstatusoutput(cmd)
if output[0]==0:

 print(output[1])

else:
  print("Some Error Occured Please Contact Admin")

