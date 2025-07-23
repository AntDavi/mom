import tkinter as tk
from tkinter import messagebox
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

class BrokerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Broker - Monitoramento")
        self.root.geometry("500x400")

        self.label_info = tk.Label(root, text="Broker MOM", font=("Arial", 16))
        self.label_info.pack(pady=10)

        self.btn_list = tk.Button(root, text="Listar Filas e Tópicos", command=self.listar)
        self.btn_list.pack(pady=5)

        self.text_output = tk.Text(root, height=20, width=60)
        self.text_output.pack(pady=5)

    def listar(self):
        result = send(LIST)
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrokerGUI(root)
    root.mainloop()
