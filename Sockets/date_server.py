import socket
import time


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('127.0.0.1', 15243))
print("Server is connected")
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''

    while True:
        conn.send("Date?")
        data = conn.recv(4096)
        if not data:
            break
        from_client = data
        time.sleep(1)
        print(from_client)
