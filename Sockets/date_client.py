import socket
import datetime
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 15243))
print("Client is connected")

while True:
    from_server = client.recv(4096)
    time.sleep(1)
    print(from_server)
    date = datetime.datetime.now()
    dateTime = str(date)
    client.send(dateTime)
