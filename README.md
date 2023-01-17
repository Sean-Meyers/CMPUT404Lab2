# CMPUT404Lab2
**Question 1: How do you specify a TCP socket in Python?**
- Either with `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` or `socket.create_connection()` or `socket.create_server()` both with default arguments. Dunno what the non-default does yet because I'm a noob.

**Question 2: What is the difference between a client socket and a server socket in Python**
- Client and server sockets are fundamentally the same objects, the main difference is that with server sockets we bind them to a host and a port and have them listen for and accept connections from clients, whereas with clients, we try to connect to servers, and try to send and receive data from them.

**Question 3: How do we instruct the OS to let us reuse the same bind port?**
- With server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1).

**Question 4: What information do we get about incoming connections?**
- The host address and the port it was assigned.

**Question 5: What is returned by recv() from the server after it is done sending the HTTP request?**
- `b'Foobar\n'`

**Question 6: Provide a link to your code on GitHub**
- https://github.com/Sean-Meyers/CMPUT404Lab2
- The files with "_demo" at the end are just notes from the lab session, and the ones without it is my code.