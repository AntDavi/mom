import sys
from broker import broker_server
from client import user_client

if __name__ == "__main__":
    modo = input("Digite 'b' para iniciar Broker ou 'c' para Cliente: ").strip().lower()
    if modo == 'b':
        broker_server.start()
    elif modo == 'c':
        user_client.__name__ == "__main__" and user_client.__main__()
