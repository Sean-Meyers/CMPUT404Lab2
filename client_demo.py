# What the TA (?) wrote during the lab, along with my own notes from watching him:
import socket

BYTES_TO_READ = 4096    # One of the biggest reasons to receive requests in small chunks like this is that if we try to take a large amount of data and it gets interrupted, our data could get corrupted.

def get(host, port):
    request = b"GET / HTTP/1.1\nHost:" + host.encode("utf-8") + b"\n\n"     # \r is redundant apparently,   encoding the host is to make sure that it's bytes in the string, this wouldn't be necessary if directly wrote the host string in the string, but because we're appending, we need this.

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a stream socket to connect to the internet. or someting...
    s.connect((host,port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)
    result = s.recv(BYTES_TO_READ)
    while(len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)

    s.close()

get("www.google.com", 80)