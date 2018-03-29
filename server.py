import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',8889))
server_socket.listen(128)
client_socket,addr=server_socket.accept()
data=client_socket.recv(4096)
print(data.decode())