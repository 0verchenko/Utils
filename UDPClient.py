import socket

# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP = input('Enter a destination IP: ')
port = int(input('Enter a port number: '))
while True:
    print('Enter a message or click Enter to exit:')
    message = input()
    if message == '':
        break
    else:
        print("UDP target IP:", IP)
        print("UDP target port:", port)
        print("message:", message)
        sock.sendto(bytes(message, "utf-8"), (IP, port))