import tkinter as tk
from common.protocol import *
import socket

HOST = 'localhost'
PORT = 5000

def send(command, *args):
    msg = format_message(command, *args)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(msg.encode())
        return s.recv(4096).decode()

def executar():
    usuario = entry_nome.get()
    to = entry_destino.get()
    msg = entry_msg.get()
    output.set(send(SEND_USER, to, msg))

root = tk.Tk()
root.title("Cliente GUI")

tk.Label(root, text="Seu nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Para quem:").pack()
entry_destino = tk.Entry(root)
entry_destino.pack()

tk.Label(root, text="Mensagem:").pack()
entry_msg = tk.Entry(root)
entry_msg.pack()

tk.Button(root, text="Enviar", command=executar).pack()
output = tk.StringVar()
tk.Label(root, textvariable=output).pack()
root.mainloop()