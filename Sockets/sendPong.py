import socket
import time

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('192.168.1.175', 8080))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''

    while True:
        data = conn.recv(4096)
        if not data:
            break
        from_client = data
        time.sleep(.5)
        print(from_client)
        conn.send("Pong")
