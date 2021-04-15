#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi
name= "date"
form = cgi.FieldStorage()
vid = form.getvalue("vid")
region = form.getvalue("region")
access_key = form.getvalue("akey")
secret_key = form.getvalue("skey")
instanceid = form.getvalue("iid")
device = form.getvalue("device")
cmd="AWS_ACCESS_KEY_ID={0} AWS_SECRET_ACCESS_KEY={1} aws ec2 attach-volume --volume-id {2} --instance-id {3} --device {4}   --region {5} --output text".format(access_key,secret_key,vid,instanceid,device,region)
output = sp.getstatusoutput(cmd)
if output[0]==0:
 
 print(output[1])

else:
   print(output[1])
   print("Some Error Occured Please Contact Admin")

