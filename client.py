import socket

# open an IP (AF_INET) USP (SOCK_DGRAM) socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send bytes to localhost address and port 5000 from a utf-g encoded string
s.sendto('hello'.encode('utf-8'), ('127.0.0.1', 5000))

# receive up to 64 bytes of data from the socket buffer
data, addr = s.recvfrom(64)

# print out the received message after decoding the string from utf-8 encoded bytes
print("Received reply: '%s' from %s" % (data.decode('utf-8'), addr))