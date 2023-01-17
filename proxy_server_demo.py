# What the TA (?) wrote during the lab, along with my own notes from watching him:
# see github.com/aianta/cmput404-tcp-lab
import socket
from threading import Thread

BYTES_TO_READ = 4096
PROXY_SERVER_HOST = "127.0.0.1"  # aka 0.0.0.0 aka localhost
PROXY_SERVER_PORT = 8080

# All our requests will go to google.com, which is our proxy target.
# Proxy client will make request to proxy server
# Proxy server will accept request and forward it to google.com
# Google will respon to proxy server, which will forward the response to proxy client

def send_request(host, port, request_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host,port))
        client_socket.send(request_data)
        client_socket.shutdown(socket.SHUT_WR)

        # get from google
        data = client_socket.recv(BYTES_TO_READ)
        result = b'' + data
        while len(data) > 0:
            data = client_socket.recv(BYTES_TO_READ)
            result += data

        return result


def handle_connection(conn, addr):
    with conn:
        print(f"Connected by: {addr}")

        request = b''
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            request += data

        reponse = send_request('www.google.com', 80, request)
        conn.sendall(response)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        serevr_socket.bind((PROXY_SERVER_HOST,PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        conn, addr = server_socket.accept()

        handle_connection(conn, addr)


def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        serevr_socket.bind((PROXY_SERVER_HOST,PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)

        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn,addr))
            thread.run()


#start_server()

start_threaded_server()