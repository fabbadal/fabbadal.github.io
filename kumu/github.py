#!/usr/bin/python2
import os
os.system("git clone https://github.com/fabbadal/fabbadal.github.io")
os.system("pwd")
os.chdir("/root/Desktop/fabbadal/fabbadal.github.io")
os.system("pwd")
print "press 1 if you have made changes"
ch=raw_input("Enter")
if int(ch)==1:
    
    os.system("git add --all")
    os.system("git commit -m \"Initial commit\"")
    os.system(" git push -u origin master")
raw_input()

