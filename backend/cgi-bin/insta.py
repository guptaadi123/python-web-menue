#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi
name= "date"
form = cgi.FieldStorage()
region = form.getvalue("region")
access_key = form.getvalue("akey")
secret_key = form.getvalue("skey")
sid = form.getvalue("sid")
itype =form.getvalue("itype")
imid=form.getvalue("imid")
key=form.getvalue("key")
count=form.getvalue("count")
subid=form.getvalue("subid")

cmd="AWS_ACCESS_KEY_ID={0} AWS_SECRET_ACCESS_KEY={1} aws ec2 run-instances --image-id {4} --count {6} --instance-type {3} --key-name {5}  --security-group-ids   {2}        --subnet-id {7}   --region {8} --output text".format(access_key,secret_key,sid,itype,imid,key,count,subid,region)
output = sp.getstatusoutput(cmd)
if output[0]==0:
 
 print(output[1])

else:
   print("Some Error Occured Please Contact Admin")

