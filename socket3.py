import socket
s=socket.socket()
print("Socket Successfully created ")
port=40674
s.bind(('',port))
print("Socket binded to %s" %(port))
s.listen(5)
print("Socket is listening")
while True:
	c,addr=s.accept()
	print("Got connected from",addr)
	c.send(b'Thanks you for connecting')
	c.close()