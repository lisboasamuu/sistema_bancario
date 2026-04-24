# 🏦 Sistema Bancário em Python

Sistema simples de gerenciamento bancário com persistência de dados em JSON, desenvolvido para fins de estudo e prática de programação orientada a objetos, manipulação de arquivos e estruturação de projetos.

## ✨ Funcionalidades

- Criar conta (CPF e nome do titular)
- Depositar valores
- Sacar valores (com verificação de saldo)
- Transferir valores entre contas
- Consultar saldo
- Visualizar histórico de movimentações (depósitos, saques, transferências)
- Listar todas as contas cadastradas
- Persistência automática dos dados em arquivo JSON
- Carregamento automático dos dados ao iniciar o programa

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- Módulo `json` para persistência
- Apenas bibliotecas padrão – sem dependências externas

## 📁 Estrutura do projeto
sistema_bancario/
├── src/ # Código fonte
│ ├── init.py # Torna src um pacote
│ ├── main.py # Loop principal e menu interativo
│ ├── banco.py # Classe Banco (gerenciamento de contas)
│ ├── conta.py # Classe Conta (lógica de operações)
│ ├── storage.py # Classe JSONStorage (leitura/escrita JSON)
│ └── utils.py # Funções auxiliares (ex: normalizar CPF)
├── data/ # Dados persistentes
│ └── banco_dados.json # Arquivo gerado automaticamente
├── tests/ # (Opcional) Testes unitários
├── README.md
├── LICENSE
├── .gitignore
├── .gitattributes
└── run.py # Script de entrada na raiz


## 🚀 Como executar

### 1. Clone ou baixe o repositório

git clone https://github.com/seu-usuario/sistema_bancario.git
cd sistema_bancario
python run.py
Ou alternativamente:
python -m src.main

Siga o menu
==================================================
          🏦 SISTEMA BANCÁRIO
==================================================
1️⃣  Criar nova conta
2️⃣  Depositar
3️⃣  Sacar
4️⃣  Transferir
5️⃣  Consultar saldo
6️⃣  Ver histórico de movimentações
7️⃣  Listar todas as contas
0️⃣  Sair
==================================================

## 💾 Persistência
Os dados são salvos automaticamente em data/banco_dados.json após cada operação que modifica o estado (criar conta, depositar, sacar, transferir).

Ao iniciar, o banco carrega automaticamente o arquivo JSON se ele existir.

O formato JSON é legível e pode ser editado manualmente (com cuidado).

🔧 Requisitos
Python 3.10 ou superior (testado com 3.12)

Nenhuma biblioteca externa necessária

## 🐛 Possíveis problemas e soluções
Problema	S
KeyError: 'historico' ao carregar dados	O JSON foi gerado por uma versão antiga. Apague data/banco_dados.json e recrie as contas, ou adicione "historico": [] manualmente no arquivo.


Erro ao depositar/sacar/transferir com valores negativos:	O programa bloqueia valores negativos e exibe mensagem de erro.

### 📝 Licença
Este projeto está sob a licença MIT – veja o arquivo LICENSE para detalhes.

### 👤 Autor
Samuel Lisboa - @lisboasamuu

## 📌 Melhorias futuras (ideias)
Limitar número de transferências por dia

Gerar extrato em PDF

Interface gráfica (Tkinter ou PyQt)

Suporte a contas poupança e corrente com regras diferentes

Autenticação com senha por conta