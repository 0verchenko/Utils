import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 13000)
print('Connecting to %s port %s' % server_address)
sock.connect(server_address)
try:
    # Send data
    message = 'Hello! '*5
    print('Sending %s' % message)
    sock.sendall(bytes(message, "UTF-8"))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print('Received "%s"' % data)
finally:
    print('Closing socket')
    sock.close()