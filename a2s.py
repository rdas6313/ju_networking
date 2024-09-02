# Question 2 file (not completed) sever

import socket
import os.path as path

host = ''
port = 20102


def sendFile(conn, name):
    with open(name, 'rb') as file:
        data = file.read(1024)
        count = 0
        while data:
            count += len(data)
            conn.send(data)
            print(f"Sent {count} bytes", end='\n')
            data = file.read(1024)
    print(f"File {name} sent successfully")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    print("Listening!")
    conn, addr = sock.accept()
    with conn:
        print(f"Connected by {addr}")
        name = conn.recv(1024).decode()

        if name and not path.isfile(name):
            conn.send(b'N')
        elif name and path.isfile(name):
            print(f"Requested file: {name}")
            conn.send(b'Y')
            sendFile(conn, name)
        print(f"Closing connection with {addr}")
    print("Closing socket")
