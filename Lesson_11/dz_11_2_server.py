import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 60000))
sock.listen(10)
print("Server is running, press CTRL+C to stop")

conn, addr = sock.accept()
print("Received connection from:", addr)

answers = {
    "hello": "Greetings! How may i serve You?",
    "who are you?": "I am limited chat-bot",
    "1": "Today a heavy rain is expected",
    "2": "Quatar football championship is the nearest big sports event",
    "3": "bye, please, press CTRL+C to stop the chat"}


def chat_bot(message):
    message = answers.get(message)
    if message:
        print(f"auto-response to client: {message}")
        return message
    else:
        message = "please, enter 1 for weather forecast, 2 for sport news, 3 to say bye"
        print("Instructions sent")
        return message


while True:
    print("Awaiting for the client inquiry")
    message = conn.recv(1024)
    message = message.decode()
    print("Client:", message)
    conn.send(chat_bot(message).encode())
conn.close()
