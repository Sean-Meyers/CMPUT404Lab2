import socket

CHUNK_SIZE = 4096
REQUEST = b'GET / HTTP/1.1\nHost: www.google.com\n\n'
HOST = 'localhost'
PORT = 8080

def get(host, port):
    """Send REQUEST to host:port, then return the response."""
    with socket.create_connection((host,port)) as sock:
        sock.send(REQUEST)
        sock.shutdown(socket.SHUT_WR)
        print("Waiting for response...")

        chunk = sock.recv(CHUNK_SIZE)
        result = b''
        while len(chunk):
            result += chunk
            chunk = sock.recv(CHUNK_SIZE)

    return result

print(get(HOST, PORT))