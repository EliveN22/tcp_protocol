import socket
import matplotlib.pyplot as plt

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12000))
server_socket.listen(1)

print("Server is ready to connect  :))")

connection_socket, addr = server_socket.accept()
print(f"Connected client: {addr}")

plt.ion()
fig, ax = plt.subplots()
x_data = []
y_data = []

try:
    while True:

        message = connection_socket.recv(1024).decode()
        if not message:
            break
        number = float(message)
        print("Received message:", number)

        y_data.append(number)
        x_data.append(len(y_data))

        ax.clear()
        ax.plot(x_data, y_data, label='Received Data')
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Random Number')
        ax.set_title('Data Graph')
        ax.legend()
        plt.draw()
        plt.pause(0.1)
finally:
    connection_socket.close()
    server_socket.close()

