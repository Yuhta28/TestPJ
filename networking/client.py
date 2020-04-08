import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 49155
BUFFER_SIZE = 1024
MESSAGE = b"Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Generete socekt(IP v4) and TCP
s.connect((TCP_IP, TCP_PORT))   # Specify IP address and port
s.send(MESSAGE) # Send Message
data = s.recv(BUFFER_SIZE)  #receive  buffer size
s.close()

print("received data", data)