import tkinter as tk
from broker.message_queue import MessageBroker

broker = MessageBroker()

def atualizar():
    filas = broker.list_queues()
    topicos = broker.list_topics()
    texto.set("Filas:\n" + "\n".join(filas) + "\n\nTópicos:\n" + "\n".join(topicos))

janela = tk.Tk()
janela.title("Broker GUI")
texto = tk.StringVar()
tk.Label(janela, textvariable=texto, justify=tk.LEFT).pack(padx=10, pady=10)
tk.Button(janela, text="Atualizar", command=atualizar).pack()
janela.mainloop()