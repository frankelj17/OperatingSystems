import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 15243))

while True:
    client.send("Ping")
    time.sleep(1)

    from_server = client.recv(4096)
    print(from_server)
