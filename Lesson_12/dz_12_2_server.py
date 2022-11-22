import asyncio
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 60000))
sock.listen(10)
print("Server is running, press CTRL+C to stop")

conn, addr = sock.accept()
print("Received connection from:", addr)

greeting = "Hello! You are connected to Server."
conn.send(greeting.encode())


async def regular_numbers(data):
    first_number, second_number = [data[i] for i in (0, 1)]
    operation = f"{first_number} + {second_number} = {first_number + second_number}"
    await asyncio.sleep(1)
    operation = f"{first_number} - {second_number} = {first_number - second_number}"
    message = operation
    return message


async def multi_numbers():
    first_number, second_number = [data[i] for i in (0, 1)]
    operation = f"{first_number} * {second_number} = {first_number * second_number}"
    await asyncio.sleep(3)
    operation = f"{first_number} / {second_number} = {first_number / second_number}"
    message = operation
    return message


while True:
    print("Awaiting for the client inquiry")
    message = conn.recv(1024)
    message = message.decode()
    print("Client:", message)
    data = message.split()
    coroutine = regular_numbers(list)
    coroutine.send(None)
    coroutine = multi_numbers(list)
    coroutine.send(None)
    conn.send(message.encode())
conn.close()