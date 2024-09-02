import socket

host = ''
port = 24000
des_port = 8000
data = True
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((host, port))
    while data:
        data = input('> ')
        if not data or data == 'q':
            break
        sock.sendto(data.encode(), (host, des_port))
        print(f"Sent data: {data}")
        ack, addr = sock.recvfrom(1024)
        print(f"Recived ack: {ack.decode()}")
