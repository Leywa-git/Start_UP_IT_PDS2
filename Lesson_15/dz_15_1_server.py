import socket
import logging


def main():
    logger = logging.getLogger("dz_15_1_logger.conf")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("dz_15_1.log")

    formatter = logging.Formatter('server %(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("", 60000))
        sock.listen(10)
        print("Server is running, press CTRL+C to stop")

        conn, addr = sock.accept()
        print("Received connection from:", addr)

        greeting = "Hello! You are connected to Server."
        conn.send(greeting.encode())
        logging.info("Server is up")
    except Exception:
        logging.error("Server does not respond")

    while True:
        print("Awaiting for the client inquiry")
        message = conn.recv(1024)
        message = message.decode()
        print("Client:", message)
        if message == "get lost":
            logging.warning("avoid client in the future")
        message = input("Enter the answer: ")
        conn.send(message.encode())
    conn.close()


if __name__ == "__main__":
    main()
