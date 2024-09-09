import socket

server_socket = socket.socket()

host = '127.0.0.1'
port = 8080

server_socket.bind((host, port))

server_socket.listen(1)
print('Server listening on {}:{}'.format(host, port))

client_socket, client_address = server_socket.accept()
print('Connection from {}'.format(client_address))

client_socket.send(b"Hello, Client!")

client_socket.close()
server_socket.close()

