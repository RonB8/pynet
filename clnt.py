import socket

print("Ahalan")
exit(0)

soc = socket.socket()

host = '127.0.0.1'
port = 8080

soc.connect((host, port))

print(soc.recv(1024).decode())

soc.close()
