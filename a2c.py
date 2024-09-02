# Question 2 (not completed) client

import socket


def saveFile(sock, name='tmp'):
    data = True
    count = 0

    with open(name, 'wb') as f:
        while data:
            data = sock.recv(1024)
            if data:
                count += len(data)
                print(f"Received {count} bytes")
                f.write(data)

    if count > 0:
        print(f"File saved successfully")
    else:
        print("No data received")


host = ''
port = 20102

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    name = input('File name: ')
    if name != 'q':
        sock.send(name.encode())
        data = sock.recv(1).decode()
        if not data:
            print("Closing client socket!")
        elif data == 'N':
            print(f'{name} not found')
        else:
            name = name + '_'
            saveFile(sock, name)
