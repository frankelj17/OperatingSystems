import socket
import datetime
import time

# socket creates a server, called server
# AF_INET = allows the server to connect to IP address
# SOCK_STREAM = allows the server to connect to a TCP port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 15243))  # Creates a server on this IP address
# 127.0.0.1 is localhost so it stays on the same machine
# binds the server to port 15243
print("Server is connected")

server.listen(1)
# Looks for one connection from client

# While the server is connected
while True:
    connection, address = server.accept()  # Accepts a connection from the client
    from_client = ''
    while True:  # While the client is connected to the server's IP
        connection.send("Ping \nDate?")  # Send Ping and Date? to the client
        # Receive 4096 bits from the client
        data_from_client = connection.recv(4096)
        time.sleep(1)
        print(data_from_client)  # Print the data received from the client
