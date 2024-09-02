import socket
import os.path as path

host = ''
port = 8080

response_template = """HTTP/1.1 {res_code} {res_msg}
Content-Length: {length}
Content-Type: text/html
Connection: close

{content}
"""


def getFile(name):
    content = ''
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            content += line
    return content


def generate(req):
    if req.startswith('GET'):
        page = req.split(' ')[1].lstrip('/')
        print(f"Requested page: {page}")
        if not path.isfile(page):
            html_content = getFile('404.html')
            code = 404
            msg = 'Not Found'
        else:
            html_content = getFile(page)
            code = 200
            msg = 'Ok'
        return response_template.format(res_code=code, res_msg=msg, length=len(html_content), content=html_content)


def handel(conn, addr):
    data = True
    with conn:
        print(f"Connected by {addr}")
        while data:
            data = conn.recv(1024).decode()
            if not data:
                print('Not received data')
                break
            else:
                response = generate(data)
                print(f"\nRequest:\n")
                print(data)
                print(f"\nResponse:\n")
                print(response)
                conn.sendall(response.encode())
        print(f"Closing connection with {addr}")


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        while True:
            print("Listening!")
            conn, addr = sock.accept()
            handel(conn, addr)
