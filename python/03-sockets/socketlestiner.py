import socket

HOST = '127.0.0.1'
PORT = 4443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
