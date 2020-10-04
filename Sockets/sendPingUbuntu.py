import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.175', 8080))

while True:
    client.send("Ping")
    time.sleep(1)
    from_server = client.recv(4096)
    print(from_server)
