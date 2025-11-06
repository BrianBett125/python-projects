# File: socket_client.py

import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
HOST = '127.0.0.1'
PORT = 65432
client_socket.connect((HOST, PORT))

# Send a message
message = "Hello Server!"
client_socket.sendall(message.encode())

# Receive a response
response = client_socket.recv(1024)
print(f"Server says: {response.decode()}")

# Close connection
client_socket.close()

