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


async def calculations(data):
    first_number, second_number = [data[i] for i in (0, 1)]
    operation = f"{first_number} + {second_number} = {first_number + second_number}"
    await asyncio.sleep(1)
    operation = f"{first_number} - {second_number} = {first_number - second_number}"
    await asyncio.sleep(2)
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
    coroutine = calculations(list)
    coroutine.send(str)
    conn.send(message.encode())
conn.close()