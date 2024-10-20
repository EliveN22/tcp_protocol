import socket
import random
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12000))

try:
    while True:
        random_number = random.randint(1, 100)
        print(f"Sending: {random_number} 😊")

        client_socket.send(str(random_number).encode())

        time.sleep(1)
finally:
    client_socket.close()

