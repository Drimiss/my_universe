import socket

def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f'Соединение с сервером {host}:{port} установлено')
    return client_socket

def get_user_input(default):
    user_input = input(f'Введите значение (по умолчанию {default}): ')
    return user_input or default


def send_data_to_server(client_socket: socket.socket, data):
    client_socket.sendall(data.encode())
    print(f'Отправлено серверу: {data}')

def receive_data_from_server(client_socket: socket.socket):
    received_data = client_socket.recv(1024).decode()
    print(f'Получено от сервера: {received_data}')


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345

    custom_host = get_user_input(HOST)
    custom_port = int(get_user_input(str(PORT)))

    client_socket = connect_to_server(custom_host, custom_port)

    try:
        while True:
            receive_data_from_server(client_socket)

            data = input('Введите строку для отправки серверу: ')
            send_data_to_server(client_socket, data)

            if data == 'exit':
                break

    finally:
        client_socket.close()