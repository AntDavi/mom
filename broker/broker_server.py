import socket
import threading
from broker.message_queue import MessageBroker
from common.protocol import *

HOST = 'localhost'
PORT = 5000
broker = MessageBroker()

def handle_client(conn, addr):
    with conn:
        print(f"[CONEXÃO] {addr} conectado.")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            command, args = parse_message(data)
            response = ""

            if command == REGISTER:
                success = broker.register_user(args[0])
                response = "OK" if success else "ERROR: Usuário já existe"

            elif command == SEND_USER:
                success = broker.send_user_message(args[0], args[1])
                response = "OK" if success else "ERROR: Usuário não encontrado"

            elif command == SUBSCRIBE:
                broker.subscribe_user_to_topic(args[0], args[1])
                response = "OK"

            elif command == PUBLISH:
                broker.publish_to_topic(args[0], args[1])
                response = "OK"

            elif command == LIST:
                response = "Filas: " + str(broker.list_queues()) + "\nTópicos: " + str(broker.list_topics())

            elif command == COUNT:
                response = str(broker.count_queue_messages(args[0]))

            elif command == "GET_MESSAGES":
                msgs = broker.get_messages(args[0])
                response = "\n".join(msgs) if msgs else "Sem mensagens."

            else:
                response = "Comando não reconhecido"

            conn.sendall(response.encode())

def start():
    print(f"[INICIANDO] Servidor Broker em {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start()
