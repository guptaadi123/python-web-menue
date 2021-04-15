#!/usr/bin/python3

print("content-type: text/html")
print()


import subprocess as sp

yum_status=sp.getstatusoutput("sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
if yum_status[0] == 0 :
 print("configured yum")
else:
 print("error in configureation")
 exit()
