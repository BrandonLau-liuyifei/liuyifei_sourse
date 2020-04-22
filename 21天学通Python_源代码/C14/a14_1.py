import socket

HOST = ''
PORT = 10888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Client\'s Address:', addr)
while True:
    data = conn.recv(1024)
    print("Receive Data:",data.decode('utf-8'))
    if not data:
        break
    conn.sendall(data)
conn.close()
