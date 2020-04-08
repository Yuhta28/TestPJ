import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 49155
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Generete socekt(IP v4) and TCP
s.bind((TCP_IP, TCP_PORT))   # Specify IP address and port
s.listen(1)     # Prepare to connect socket

conn, addr = s.accept() # Wait for connection socket
print("Connection address:", addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("received data:", data)
    conn.send(data) # echo
conn.close()