#!/usr/bin/python
import os

os.system("tput setaf 3")
print "Welcome to the FabCloud"
print "-----------------------"
os.system("tput setaf 0")

print """
press 1: For SaaS (Software as a service)
press 2: For StaaS(Storage as a service)
"""

x=raw_input("Enter your choice")

if int(x)==1:
	print """
	press 1:For Firefox
	press 2:For Calculator
	press 3:For vlc
	"""
	y=raw_input("enter your choice")
	name=raw_input("enter username")
	if int(y)==1:
		os.system("ssh -X -l {} 192.168.1.12 firefox".format(name))
	elif int(y)==2:
		os.system("ssh -X -l {} 192.168.1.12  gnome-calculator".format(name))
	else:
		os.system("ssh -X -l {} 192.168.1.12 vlc".format(name))
else:
	print """
	press 1:For Object Storage 
	press 2:For Block Storage
	"""

aa=raw_input()
