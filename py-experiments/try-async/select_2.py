import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5001))
    server_socket.listen()

    selector.register(
        fileobj=server_socket,
        events=selectors.EVENT_READ,
        data=accept_connection,
    )


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print("Connetction from", addr)

    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_meassage,
    )


def send_meassage(client_socket):
    request = client_socket.recv(4066)
    if request:
        response = b"Hello World!\n"
        client_socket.sendall(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        event = selector.select()[0][0]
        callback = event.data
        callback(event.fileobj)


if __name__ == "__main__":
    server()
    event_loop()
