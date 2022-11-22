import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 60000))

while True:
    message = (sock.recv(1024)).decode()
    print("Server:", message)
    message = input("Enter the message: ")
    print("Awaiting for a reply")
    sock.send(message.encode())
sock.close()