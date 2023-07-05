import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 60000))
sock.listen(10)
print("Server is running, press CTRL+C to stop")

conn, addr = sock.accept()
print("Received connection from:", addr)

greeting = "Hello! You are connected to Server."
conn.send(greeting.encode())

while True:
    print("Awaiting for the client inquiry")
    message = conn.recv(1024)
    message = message.decode()
    print("Client:", message)
    message = input("Enter the answer: ")
    conn.send(message.encode())
conn.close()
