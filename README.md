# 🏦 Sistema Bancário em Python

> 💡 Projeto com arquitetura preparada para evolução em API REST ou aplicação desktop completa.

Sistema de gerenciamento bancário com **duas interfaces (CLI e GUI)** e **persistência em JSON**.

Projeto desenvolvido com foco em:
- Programação Orientada a Objetos (POO)
- Estruturação de projetos reais em Python
- Manipulação de arquivos e serialização (JSON)
- Interface gráfica com Tkinter

---

## ✨ Funcionalidades

- Criar conta (CPF + nome)
- Depositar valores
- Sacar com validação de saldo
- Transferir entre contas
- Consultar saldo
- Visualizar histórico de transações
- Listar contas cadastradas

### 🔄 Persistência automática
- Salvamento após cada operação
- Carregamento automático ao iniciar

### 🖥️ Interfaces disponíveis
- CLI (terminal com menu numérico)
- GUI (interface gráfica com Tkinter)

---

## 🛠️ Tecnologias

- Python 3.10+
- json (persistência de dados)
- tkinter (GUI nativa)
- Sem dependências externas

---

## 📁 Estrutura do Projeto

sistema_bancario/
├── src/
│   ├── banco.py
│   ├── conta.py
│   ├── storage.py
│   ├── utils.py
│   ├── main.py
│   └── gui.py
├── data/
│   └── banco_dados.json
├── tests/
├── run.py
├── run_gui.py
├── README.md
├── LICENSE
└── .gitignore

---

## 🚀 Como Executar

### 1. Clone o repositório

git clone https://github.com/seu-usuario/sistema_bancario.git
cd sistema_bancario

### 2. Escolha a interface

#### 🖥️ Terminal

python run.py

ou

python -m src.main

#### 🖱️ Interface gráfica

python run_gui.py

ou

python -m src.gui

---

## 🧭 Uso

### CLI (Terminal)

1 - Criar conta  
2 - Depositar  
3 - Sacar  
4 - Transferir  
5 - Consultar saldo  
6 - Ver histórico  
7 - Listar contas  
0 - Sair  

### GUI

- Interface com botões para cada operação
- Inputs via janelas secundárias
- Feedback com pop-ups
- Salvamento automático

---

## 💾 Persistência

Arquivo de dados:

data/banco_dados.json

- Atualizado automaticamente
- Pode ser editado manualmente (com cautela)

---

## 🔧 Requisitos

- Python 3.10+

---

## 🐛 Problemas comuns

Problema: KeyError: 'historico'  
Solução: Recrie o JSON ou adicione "historico": []

Problema: Botões estranhos na GUI  
Solução: Use tk.Button em vez de ttk.Button

Problema: CPF não encontrado  
Solução: O sistema remove formatação automaticamente

---

## 📌 Melhorias futuras

- Limite de transferências por dia
- Exportação de extrato em PDF
- Autenticação por senha
- Tipos de conta (corrente/poupança)
- API REST (Flask ou FastAPI)

---

## 🧠 Arquitetura

- Separação de responsabilidades:
  - Banco → regras de negócio
  - Conta → operações e histórico
  - Storage → persistência

- Baixo acoplamento
- Estrutura pronta para escalar
- Reutilização da lógica entre CLI e GUI

---

## 👤 Autor

Samuel Lisboa  
https://github.com/lisboasamuu

---

## 📄 Licença

MIT License

---

## 🤝 Contribuição

Pull requests e sugestões são bem-vindos.