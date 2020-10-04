import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 15243))
print("Client is connected")

while True:
    client.send("Ping \nDate?")
