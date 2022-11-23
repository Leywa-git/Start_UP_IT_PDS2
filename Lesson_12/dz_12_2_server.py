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

    greeting = "Hello! You are connected to Server.\n" \
               "Enter q in order to disconnect from Server.\n" \
               "Enter 2 numbers to receive equations with them."

    conn.send(greeting.encode())

    message = conn.recv(1024)
    message = message.decode()
    print("Client:", message)

    while message != "quit":
        message = conn.recv(1024)
        message = message.decode()
        print("Client:", message)
        data = message.split()
        loop = asyncio.get_event_loop()
        equation_1 = loop.create_task(addition())
        equation_2 = loop.create_task(subtraction())
        equation_3 = loop.create_task(multiply())
        equations_await = asyncio.wait(equation_1)
        loop.run_until_complete()
        result = f"{equation_1} \n" \
                 f"{equation_2} \n" \
                 f"{equation_3}"
        conn.send(message.encode())
    conn.close()


asyncio.run(server())
