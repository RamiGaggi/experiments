import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        print('Before .accept()')
        client_socket, addr = server_socket.accept()
        print('Connetction from', addr)
        
        while True:
            request = client_socket.recv(4066)

            if not request:
                break
            else:
                response = b'Hello World!\n'
                client_socket.sendall(response)
        
        print('Outside inner while loop')
        client_socket.close()
        


if __name__ == '__main__':
    main()
