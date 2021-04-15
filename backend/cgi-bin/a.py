#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi
name= "date"
form = cgi.FieldStorage()
key_name = form.getvalue("key")
region = form.getvalue("region")
access_key = form.getvalue("akey")
secret_key = form.getvalue("skey")
cmd="AWS_ACCESS_KEY_ID={0} AWS_SECRET_ACCESS_KEY={1} aws ec2 create-key-pair --key-name {2}   --region {3}".format(access_key,secret_key,key_name,region)
output = sp.getstatusoutput(cmd)
print(output)
