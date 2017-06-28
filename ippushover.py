#!/usr/bin/python
#############################################################################
#
# ippushover.py                                    
#
# Description:
#  
#	This program will determine the IP address of the machine running
#       it and use the API service of pushover.net to send this information
#       out. 
#	I put this program at the end of /etc/profile of my Raspberry Pi.
#       When the Pi boots up, it will use this to tell me the IP. I can use
#       that information to SSh into the Pi.
#
# History:
#
#       2017.07.26	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python ippushover.py
#############################################################################

# Initialization of variables, etc.

# Since this program is run at boot time typically, I like to have these 
# print statements to tell me that this program is about to run.

print("******************************************")
print("*   Calling ippushover.py                *")
print("******************************************")

import sys, subprocess, httplib, urllib, socket

# Use socket to determine your IP address that can access the Internet
# (8.8.8.8) being the IP address for Google's DNS server.
# Store the IP addressn my_IP 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
my_IP = s.getsockname()[0]

# The following variables are required when calling API of pushover.net
myTitle = "IP Pushover Notification"
myMessage = "The IP address is " + my_IP
myPushoverToken = "<put your token here>"
myPushoverUserID = "<put your ID here>"
	

conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": myPushoverToken,
    "user": myPushoverUserID,
	"title": myTitle,
    "message": myMessage,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()

sys.exit(0)
