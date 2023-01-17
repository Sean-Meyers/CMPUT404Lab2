import socket

HOST = 'www.google.com'
PORT = 'http'

with socket.create_connection((HOST, PORT)) as sock:
    # Some stuff here is by TRIANGLES from https://internalpointers.com/post/making-http-requests-sockets-python#:~:text=Python%27s%20HTTP%20request%3A%20first%20attempts%201%201.%20Configuring,server%20...%205%205.%20Closing%20the%20socket%20
    sock.send(b"GET / HTTP/1.0\r\n\r\n")
    data = b""
    while True:
        chunk = sock.recv(4096)
        if len(chunk) == 0:     # No more data
            break
        data += chunk
print(repr(data))