# Question 1
import socket

host = '127.0.0.1'
port = 10201

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    print(f"Connected to host {host} and ip {port}")
    data = True
    while data:
        data = input('> ')
        sock.send(data.encode())
        if data == 'q':
            break
    data = sock.recv(1024).decode()

print(f"Received data: {data}")
