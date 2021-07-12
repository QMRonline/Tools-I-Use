import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("QMART Script")
print(ascii_banner)

# Defining a target
if len(sys.argv) == 2:

	# translate hostname to IPv4
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid ammount Argument Needed An IP Addr use command if Windows use IP Address if Linux use ifconfig / ip addr")

# Add Banner
print("-" * 50)
print("Your Target: " + target)
print("Scanning start time:" + str(datetime.now()))
print("-" * 50)

try:

	# will scan ports between 1 to 65,535 you can change if needed
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		# returns an error indicator
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
		print("\n Keyboard interrupted ")
		sys.exit()
except socket.gaierror:
		print("\n Hostname Could Not Be Resolved ")
		sys.exit()
except socket.error:
		print("\ Server not responding, Try to ping the IP Address")
		sys.exit()
