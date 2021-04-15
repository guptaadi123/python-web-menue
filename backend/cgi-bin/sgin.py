#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi
name= "date"
form = cgi.FieldStorage()
sg_name = form.getvalue("sg_name")
protocol= form.getvalue("prot")
cidr= form.getvalue("cidr")
port= form.getvalue("port")
region = form.getvalue("region")
access_key = form.getvalue("akey")
secret_key = form.getvalue("skey")

cmd="AWS_ACCESS_KEY_ID={0} AWS_SECRET_ACCESS_KEY={1} aws ec2 authorize-security-group-ingress --group-name {2} --protocol    {3} --port {4} --cidr {5}   --region {6}   --output text ".format(access_key,secret_key,sg_name,protocol,port,cidr,region)
output = sp.getstatusoutput(cmd)
if output[0]==0:

 print(output[1])
 print("Suceully created your request")


else:
  print("Some Error Occured Please Contact Admin")

