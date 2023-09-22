import socket

ip = '127.0.0.1'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.connect((ip, port))
    s.sendall(b'hello server')
    data = s.recv(1024)
print('receive message from server :', data.decode("uft-8"))
