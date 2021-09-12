import socket
from views import index, blog

URLS = {
    '/': index,
    '/blog': blog,
}


def parse_request(request):
    parsed = request.split()
    method = parsed[0]
    url = parsed[1]
    return (method, url)


def generate_headers(method, url):
    if method != 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)
    if url not in URLS:
        return ('HTTP/1.1 404 Not Found\n\n', 404)
    return ('HTTP/1.1 200 OK\nMySuccesHeader: OK\n\n', 200)


def generate_content(code, url):
    if code == 404:
        return '<h1>404 Not found<h1>'
    if code == 405:
        return '<h1>405 Method not found<h1>'
    return URLS[url]()
    



def generate_response(request):
    method, url = parse_request(request.decode('utf-8'))
    headers, code = generate_headers(method, url)
    
    body = generate_content(code, url)
    
    return (headers + body).encode()

# AF_ INET - protocol IP4
# SOCK_STREAM - TCP protocol
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()
    
    while True:
        client_socket, addr  = server_socket.accept()
        print(f'{addr} connected to the server')
        request = client_socket.recv(1024)
        print(request)
        
        response = generate_response(request)

        
        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    main()