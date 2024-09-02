# Question 1
import socket

host = '127.0.0.1'
port = 10201


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    print(f"Tcp server started! Listening on ip {host} and port {port}")
    conn, addr = sock.accept()
    with conn:
        print(f"Connected with ip {addr[0]} and port {addr[1]}")
        while True:
            data = conn.recv(1024).decode()
            if data == 'q':
                break
            print(f"Received data: {data}")
        conn.sendall(b'Received all data!')
        print(f"Closed connection {addr}")
    print("Closing socket")
