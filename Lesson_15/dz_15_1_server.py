import socket
import logging
import dz

module_logger = logging.getLogger("Server_Log")

fh = logging.FileHandler("Server_Log")

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 60000))
    sock.listen(10)
    print("Server is running, press CTRL+C to stop")

    conn, addr = sock.accept()
    print("Received connection from:", addr)

    greeting = "Hello! You are connected to Server."
    conn.send(greeting.encode())
except Exception:
    logging.error("Server does not respond")

while True:
    print("Awaiting for the client inquiry")
    message = conn.recv(1024)
    message = message.decode()
    print("Client:", message)
    message = input("Enter the answer: ")
    conn.send(message.encode())
conn.close()
