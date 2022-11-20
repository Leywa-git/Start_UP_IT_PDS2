import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 60000))
sock.listen(10)
print("Server is running, press CTRL+C to stop")

conn, addr = sock.accept()
print("Received connection from:", addr)

greeting = "Hello! You are connected to Server.\n" \
           "Server will count words you entered.\n" \
           "Numbers are not counted"
conn.send(greeting.encode())

while True:
    message = conn.recv(1024)
    message = message.decode()
    print("Client:", message)
    data = message.split()
    print(data)
    counter = 0
    for i in data:
        if not i.isdigit():
            counter += 1
    message = f"Number of words used by Client: {counter}"
    print(counter, "words used by Client")
    conn.send(message.encode())
conn.close()
