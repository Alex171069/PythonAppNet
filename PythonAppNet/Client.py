import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8007
s.connect((host, port))
s.send('hello')  
data = s.recv(1000000) 
print('received', data, len(data), 'bytes')
s.close()
