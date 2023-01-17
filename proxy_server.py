import socket
from threading import Thread

CHUNK_SIZE = 4096
PROXY_PORT = 8080
PROXY_HOST = 'localhost'

def send_request(host, port, request):
    """
    Send request byte string to host:port.
    Return what we received from host:port (byte string).
    """

    with socket.create_connection((host, port)) as client:
        client.send(request)
        client.shutdown(socket.SHUT_WR)

        data = client.recv(CHUNK_SIZE)
        result = b''
        while len(data):
            result += data
            data = client.recv(CHUNK_SIZE)

    return result


def handle_connection(conn, addr):
    """
    Receive data from the conn socket at addr string, send it to
    http://www.google.com, then send google's response back to conn.
    """

    with conn:
        data = conn.recv(CHUNK_SIZE)
        request = b''
        while len(data):
            print(f"Received {data} from {addr}")
            request += data
            data = conn.recv(CHUNK_SIZE)

        conn.sendall(send_request('www.google.com', 'http', request))


def start_server():
    """Start the proxy server and and handle each connection in a new thread."""

    with socket.create_server((PROXY_HOST, PROXY_PORT), backlog=2) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.listen()

        while True:
            conn, addr = server.accept()
            thread = Thread(target=handle_connection, args=(conn,addr))
            thread.run()


start_server()
            
