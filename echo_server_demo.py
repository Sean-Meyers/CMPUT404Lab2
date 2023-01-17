# What the TA (?) wrote during the lab, along with my own notes from watching him:
import socket

BYTES_TO_READ = 4096
HOST = "127.0.0.1"  # aka 0.0.0.0 aka localhost
PORT = 8080

def handle_connection(conn, addr):      # conn is a serevr created socket connected to the client created by s.accpet or something
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     # reuseaddr allows us to reuse addresses when they are time out but before they have expired or something
        s.listen()

        conn, addr = s.accept()
        handle_connection(conn, addr)


start_server()