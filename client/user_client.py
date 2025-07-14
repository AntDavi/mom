import socket
from common.protocol import *

HOST = 'localhost'
PORT = 5000

def send(command, *args):
    msg = format_message(command, *args)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(msg.encode())
        data = s.recv(4096).decode()
    return data

def menu(user):
    while True:
        print(f"\nUsuário: {user}")
        print("1. Enviar mensagem para usuário")
        print("2. Assinar tópico")
        print("3. Publicar em tópico")
        print("4. Ver mensagens")
        print("5. Listar filas e tópicos")
        print("6. Contar mensagens")
        print("0. Sair")
        choice = input("> ")

        if choice == "1":
            to = input("Destinatário: ")
            msg = input("Mensagem: ")
            print(send(SEND_USER, to, msg))
        elif choice == "2":
            topic = input("Tópico: ")
            print(send(SUBSCRIBE, user, topic))
        elif choice == "3":
            topic = input("Tópico: ")
            msg = input("Mensagem: ")
            print(send(PUBLISH, topic, msg))
        elif choice == "4":
            print(send("GET_MESSAGES", user))
        elif choice == "5":
            print(send(LIST))
        elif choice == "6":
            print("Mensagens na sua fila:", send(COUNT, user))
        elif choice == "0":
            break

if __name__ == "__main__":
    nome = input("Nome de usuário: ")
    result = send(REGISTER, nome)
    if "OK" in result:
        menu(nome)
    else:
        print(result)
