import socket
import logging


def main():

    logging.basicConfig(level=logging.INFO, filename="dz_15_1.log", format="%(asctime)s - %(levelname)s - %(message)s")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 60000))
    sock.listen(10)
    print("Server is running, press CTRL+C to stop")

    conn, addr = sock.accept()
    print("Received connection from:", addr)

    greeting = "Hello! You are connected to Server. Press CTRL+C to exit the server. Type 0 if You are not interested."
    conn.send(greeting.encode())
    logging.info("Server is up")

    while True:
        print("Awaiting for the client inquiry")
        message = conn.recv(1024)
        message = message.decode()
        print("Client:", message)
        logging.info("Client:" + message)
        message = input("Enter the answer: ")
        conn.send(message.encode())
    conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("Server closed")
    except Exception:
        logging.error("Client disconnect")
