import socket
import datetime
import time

# Create a socket called client
# Same as the server, AF_INET allows connection to IP Address
# SOCK_STREAM allows to connect to a port
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the IP address and port that was binded by the server
client.connect(('127.0.0.1', 15243))
print("Client is connected")

# While the client is connected to that IP
while True:
    from_server = client.recv(4096)  # Recieve data from the server
    time.sleep(1)
    print(from_server)  # Print the data from the server
    date = datetime.datetime.now()
    dateTime = str(date)
    client.send("Pong\n" + str(dateTime))
    # Send Pong and the actual time and date to server
