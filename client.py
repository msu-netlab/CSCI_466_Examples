import socket

# open an IP (AF_INET) USP (SOCK_DGRAM) socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send bytes to localhost address and port 5000 from a utf-g encoded string
s.sendto('hello'.encode('utf-8'), ('127.0.0.1', 5000))