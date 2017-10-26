# Camada Física da Computação
# Exemplo socket server 
## https://pymotw.com/2/socket/tcp.html

import socket
import sys

class SocketClient:
    def __init__(self):
        self.porta = 1280
        print("Client: enviar dados")
        print("Inicializando socket TCP/IP")
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to the port
        server_address = ('localhost', self.porta)
        print("PORTA {}".format(self.porta))
        self.sock.connect(server_address)

    def start_socket(self, message):


        try:
            # Send data
            b = bytearray()
            b.extend(map(ord, message))
            message = b
            print(message)
            self.sock.sendall(message)

            amount_received = 0
            amount_expected = len(message)
            
            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received {}'.format(data))

        finally:
            # Clean up the connection
            print('closing socket')
            self.sock.close()


