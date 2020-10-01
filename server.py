import socket

# open an IP (AF_INET) UDP (SOCK_DGRAM) socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to localhost address and port 5000
s.bind(('127.0.0.1', 5000))

# receive up to 64 bytes of data from the socket buffer
data, addr = s.recvfrom(64)

# print out the received message after decoring the string from utf-8 encoded bytes
print("Received message: '" + data.decode('utf-8') + "'")