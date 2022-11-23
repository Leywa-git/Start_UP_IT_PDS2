import asyncio
import socket


async def addition():
    first_number, second_number = [data[i] for i in (0, 1)]
    message = f"{first_number} + {second_number} = {first_number + second_number}"
    return message


async def subtraction():
    first_number, second_number = [data[i] for i in (0, 1)]
    message = f"{first_number} - {second_number} = {first_number - second_number}"
    return message


async def multiply():
    first_number, second_number = [data[i] for i in (0, 1)]
    message = f"{first_number} * {second_number} = {first_number * second_number}"
    return message


async def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 60000))
    sock.listen(10)
    sock.setblocking(False)
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
        data = message.split()
        addition().send(data)
        subtraction().send(data)
        multiply().send(data)
        conn.send(message.encode())
    conn.close()


asyncio.run(server())
