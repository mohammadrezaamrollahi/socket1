import socket

ip = '127.0.0.1'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.bind((ip, port))
    s.listen()
    print("server is listen on %s %d" %(ip, port))
    #ساختن ارتباط

    #پذیرش
    conn, addr = s.accept()
    with conn :
        print(f'connect by {addr}')
        data = conn.recv(1024)
        print("receive message from client: ", data.decode('uft-8'))
        conn.sendall(b'hello client')

