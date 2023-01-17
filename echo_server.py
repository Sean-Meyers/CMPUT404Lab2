import socket

HOST = 'localhost'
PORT = 8001

with socket.create_server((HOST, PORT)) as sock:
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        while True:
            print('Connected by', addr)
            data = conn.recv(1024)
            if not data: break
            print('Received:', repr(data), 'from', addr)
            conn.sendall(data)