#!/usr/bin/python2
import os
os.system("tput setaf 1")
print"\t\t\t\t"
print"""
	press 1 for calculator
	press 2 for date
	press 3 for open file
	press 4 for create user
	press 5 for exit
	press 6 for any software for rent
"""
ch=raw_input("enter your choice:")

if int(ch)==1:
     print"cal"
     os.system("cal")
if int(ch)==2:
     print"date"
     os.system("date")
if int(ch)==3:
     print"open file"
if int(ch)==4:
     print"create user"
if int(ch)==5:
     print"exit"
     os.system("exit")
if int(ch)==6:
    print "software on rent"
    x=raw_input("enter the service you want for other user")
    os.system("ssh -X -l root 192.168.1.13 {}".format(x))
raw_input()
