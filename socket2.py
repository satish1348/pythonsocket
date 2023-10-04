import socket # for socket
import sys
try:
	s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("SOCKET SUCCESSFULLY  CREATED")
except socket.error as err:
	print("SOCKET CREATION FAILED WITH ERROR %s"%(err))
port =80
try:
	host_ip=socket.gethostbyname("www.google.com")
except socket.gaierror:
	print("There was an error resolving the host")
	sys.exit()
s.connect((host_ip,port))
print("The socket has successfully connected to google")