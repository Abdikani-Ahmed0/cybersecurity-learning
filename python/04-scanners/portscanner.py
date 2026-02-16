import sys
import socket
from datetime import datetime as dt

# define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid amount of arguments. ")
	print("Syntax: python3 portscanner.py <ip>")
	
# add a pretty banner
print("-" *50)
print("Scanning target " + target)
print("Time started: " + str(dt.now()))
print("-" *50)

try:
	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
	        	print("Port {} is Open".format(port))
	s.close()
	
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
	
