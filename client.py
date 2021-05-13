#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

for i in range(5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        msg = f'Hello from client:{i}'
        s.connect((HOST, PORT))
        s.sendall(msg.encode())
        data = s.recv(1024)
        # print(f'Client {i} Received {repr(data)}')