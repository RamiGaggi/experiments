import socket
from select import select

monitor = []


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 5001))
server_socket.listen()


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print("Connetction from", addr)

    monitor.append(client_socket)


def send_meassage(client_socket):
    request = client_socket.recv(4066)
    if request:
        response = b"Hello World!\n"
        client_socket.sendall(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(monitor, [], [])  #  read, write, errors

        for socket in ready_to_read:
            if socket is server_socket:
                accept_connection(socket)
            else:
                send_meassage(socket)


if __name__ == "__main__":
    monitor.append(server_socket)
    event_loop()
