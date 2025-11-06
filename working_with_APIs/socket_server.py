# File: socket_server.py

import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
HOST = '127.0.0.1'   # localhost
PORT = 65432         # arbitrary non-privileged port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen()
print(f"Server is listening on {HOST}:{PORT}...")

while True:
    # Wait for a connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Communicate with the client
    while True:
        data = conn.recv(1024)  # receive up to 1024 bytes
        if not data:
            break  # client disconnected
        print(f"Received from client: {data.decode()}")
        conn.sendall(b"Message received!")  # send a reply

    conn.close()
    print("Client disconnected.")

