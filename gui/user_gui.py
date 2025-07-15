import tkinter as tk
from tkinter import simpledialog, messagebox
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

class UserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cliente MOM")
        self.root.geometry("500x500")
        
        self.username = simpledialog.askstring("Login", "Digite seu nome de usuário:")
        if not self.username:
            root.destroy()
            return

        result = send(REGISTER, self.username)
        if "ERROR" in result:
            messagebox.showerror("Erro", result)
            root.destroy()
            return

        tk.Label(root, text=f"Bem-vindo, {self.username}", font=("Arial", 16)).pack(pady=10)

        tk.Button(root, text="Enviar mensagem direta", command=self.enviar_direto).pack(pady=4)
        tk.Button(root, text="Assinar tópico", command=self.assinar_topico).pack(pady=4)
        tk.Button(root, text="Publicar em tópico", command=self.publicar_topico).pack(pady=4)
        tk.Button(root, text="Ver mensagens", command=self.ver_mensagens).pack(pady=4)
        tk.Button(root, text="Listar filas/tópicos", command=self.listar).pack(pady=4)

        self.text_output = tk.Text(root, height=20, width=60)
        self.text_output.pack(pady=10)

    def enviar_direto(self):
        destino = simpledialog.askstring("Enviar", "Para quem?")
        msg = simpledialog.askstring("Mensagem", "Digite a mensagem:")
        if destino and msg:
            res = send(SEND_USER, destino, msg)
            self.show_output(res)

    def assinar_topico(self):
        topico = simpledialog.askstring("Assinar", "Nome do tópico:")
        if topico:
            res = send(SUBSCRIBE, self.username, topico)
            self.show_output(res)

    def publicar_topico(self):
        topico = simpledialog.askstring("Publicar", "Nome do tópico:")
        msg = simpledialog.askstring("Mensagem", "Digite a mensagem:")
        if topico and msg:
            res = send(PUBLISH, topico, msg)
            self.show_output(res)

    def ver_mensagens(self):
        res = send("GET_MESSAGES", self.username)
        self.show_output(res)

    def listar(self):
        res = send(LIST)
        self.show_output(res)

    def show_output(self, msg):
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, msg)

if __name__ == "__main__":
    root = tk.Tk()
    app = UserGUI(root)
    root.mainloop()
