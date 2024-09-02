import socket

host = ''
port = 8000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((host, port))
    print("Server listening!")
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"\nClient address: {addr}")
        print(f"Client data: {data.decode()}")
        sock.sendto('Received!'.encode(), addr)
