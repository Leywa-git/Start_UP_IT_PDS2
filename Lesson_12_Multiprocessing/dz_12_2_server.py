import asyncio
import socket


async def addition(data):
    first_number, second_number = [data[i] for i in (0, 1)]
    global message_1
    message_1 = f"{first_number} + {second_number} = {first_number + second_number}"
    return message_1


async def subtraction(data):
    first_number, second_number = [data[i] for i in (0, 1)]
    global message_2
    message_2 = f"{first_number} - {second_number} = {first_number - second_number}"
    return message_2


async def multiply(data):
    first_number, second_number = [data[i] for i in (0, 1)]
    global message_3
    message_3 = f"{first_number} * {second_number} = {first_number * second_number}"
    return message_3


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
        ioloop = asyncio.get_event_loop()
        tasks = [ioloop.create_task(addition(data)),
                 ioloop.create_task(subtraction(data)),
                 ioloop.create_task(multiply(data))]
        wait_tasks = asyncio.wait(tasks)
        ioloop.run_until_complete(wait_tasks)
        result = f"{message_1} \n" \
                 f"{message_2} \n" \
                 f"{message_3}"
        sock.send(result.encode())
    conn.close()

async def run_server():
    server = await asyncio.start_server()
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(run_server())
