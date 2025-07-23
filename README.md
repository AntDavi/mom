# 📡 MOM - Middleware Orientado a Mensagens (Python + Tkinter)

Projeto individual da disciplina de **Programação Paralela e Distribuída (IFCE, 2025.1)** com o objetivo de implementar um sistema de comunicação assíncrona utilizando **filas e tópicos**, simulando o comportamento de um **Message-Oriented Middleware (MOM)**. A comunicação é feita com **sockets TCP** em Python e a interface gráfica com **Tkinter**.

---

## 📌 Sumário

- 📷 Visão Geral
- 🚀 Execução
- 🧠 Conceitos de MOM
- 🔧 Tecnologias Utilizadas
- 📡 Comunicação em Rede
- 🗂 Estrutura de Pastas
- ⚙️ Funcionalidades Implementadas
- 📌 Observações Técnicas
- 📚 Curiosidades e Justificativas
- 👤 Autor

---

## 📷 Visão Geral

O sistema MOM permite a comunicação indireta e desacoplada entre aplicações clientes através de:

- Filas privadas: comunicação direta entre usuários (mesmo offline)
- Tópicos: mecanismo publish/subscribe para comunicação em grupo
- Gerenciamento centralizado por um **Broker**, que roteia mensagens

O projeto simula:

- Registro de usuários com verificação de duplicidade
- Filas automáticas para cada usuário
- Assinatura de tópicos
- Envio de mensagens diretas e para tópicos
- Interfaces gráficas simples para o broker e clientes

---

## 🚀 Execução

### ⚙️ Pré-requisitos

- Python 3.10 ou superior
- Compatível com Windows, Linux ou macOS

### ▶️ Rodando o projeto

```bash
# Vá até a raiz do projeto
cd mom

# Inicie o Broker
python -m broker.broker_server

# Em outro terminal, inicie um cliente (pode abrir quantos quiser)
python -m gui.user_gui

# Opcional: GUI de monitoramento do broker
python -m gui.broker_gui
```

---

## 🧠 Conceitos de MOM

- **Filas (Queues):** cada usuário possui uma fila individual de mensagens
- **Tópicos (Topics):** os usuários podem se inscrever para receber publicações
- **Broker:** servidor responsável por roteamento, entrega e gerenciamento
- **Assinatura:** usuários podem assinar tópicos para receber mensagens
- **Mensagens Offline:** se o destinatário não estiver online, a mensagem é armazenada

---

## 🔧 Tecnologias Utilizadas

- 🐍 Python 3.12
- 🖼️ Tkinter (GUI)
- 🌐 Socket TCP/IP (rede)
- 🧵 Threading (concorrência)
- 🗂 Queue (armazenamento de mensagens)
- 🔧 Protocolo simples de comandos (`REGISTER`, `PUBLISH`, etc.)

---

## 📡 Comunicação em Rede

A arquitetura é baseada no padrão **cliente-servidor** via **sockets TCP**:

- O **Broker** atua como servidor, escutando uma porta
- Os **Clientes** se conectam ao broker e trocam comandos
- Toda comunicação é **texto puro** com um protocolo leve (`COMANDO::ARG1::ARG2`)

---

## 🗂 Estrutura de Pastas

```
mom/
├── broker/
│   ├── broker_server.py       # Lógica do servidor central (Broker)
│   ├── message_queue.py       # Estrutura de filas e tópicos
├── client/
│   ├── user_client.py         # Cliente por terminal
│   ├── publisher.py           # Cliente que publica (extensível)
│   ├── subscriber.py          # Cliente que assina (extensível)
├── common/
│   └── protocol.py            # Protocolo de comunicação
├── gui/
│   ├── broker_gui.py          # Interface do broker
│   └── user_gui.py            # Interface do usuário
└── main.py                    # Entrada opcional do sistema
```

---

## ⚙️ Funcionalidades Implementadas

### ✅ Broker (Servidor)
- Registro de usuários (sem duplicidade)
- Criação automática de fila para novos usuários
- Criação e remoção de tópicos
- Envio e roteamento de mensagens
- Listagem de filas, tópicos e mensagens pendentes

### ✅ Cliente (Usuário)
- Interface gráfica (Tkinter)
- Envio de mensagens diretas (offline suportado)
- Assinatura e publicação em tópicos
- Visualização de mensagens recebidas
- Listagem de tópicos e filas disponíveis

---

## 📌 Observações Técnicas

- As interfaces foram feitas com **Tkinter** para leveza e portabilidade
- O servidor lida com múltiplos clientes via `threading.Thread`
- A fila de mensagens de cada usuário é gerenciada com `queue.Queue`
- O protocolo é baseado em **strings simples com separador "::"**
- A arquitetura permite futura adição de persistência, histórico ou autenticação

---

## 📚 Curiosidades e Justificativas

- A escolha do tema simula ambientes reais como **RabbitMQ**, **Kafka**, **ActiveMQ**
- A abordagem por tópicos permite múltiplos assinantes para uma mesma mensagem
- O uso de GUI melhora a visualização do fluxo e interação, principalmente para fins didáticos
- O projeto foi pensado para refletir o funcionamento de sistemas distribuídos modernos
- Foco no aprendizado de:
  - Comunicação assíncrona
  - Concorrência
  - Protocolo de rede customizado
  - Estruturação modular

---

## 👤 Autor

Desenvolvido por **Anthony Davi**  
Aluno do curso de Engenharia de Computação – IFCE  
Disciplina: Programação Paralela e Distribuída (2025.1)  
Professor: **Cidcley T. de Souza**  
Contato: [anthony.davi.sousa08@aluno.ifce.edu.br](mailto:anthony.davi.sousa08@aluno.ifce.edu.br)
