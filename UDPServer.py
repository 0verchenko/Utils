import socket

# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = int(input('Enter a port number: '))
server_address = ('', port)
print('Starting up on %s port %s' % server_address)

# Bind the socket to the port
sock.bind(server_address)

while True:
    # Wait for a connection
    print('Waiting for a messages')
    data, client_address = sock.recvfrom(1024)
    print('Data received %s' % data)
