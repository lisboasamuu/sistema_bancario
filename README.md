# 🏦 Sistema Bancário em Python

Sistema simples de gerenciamento bancário com persistência de dados em JSON, desenvolvido para estudo de:

* Programação Orientada a Objetos (POO)
* Manipulação de arquivos
* Estruturação de projetos reais em Python

---

## ✨ Funcionalidades

* Criar conta (CPF e nome do titular)
* Depositar valores
* Sacar valores (com verificação de saldo)
* Transferir valores entre contas
* Consultar saldo
* Visualizar histórico de movimentações
* Listar todas as contas cadastradas
* Persistência automática em JSON
* Carregamento automático ao iniciar

---

## 🛠️ Tecnologias utilizadas

* Python 3.10+
* Módulo `json` (nativo)
* Sem dependências externas

---

## 📁 Estrutura do projeto

```
sistema_bancario/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── banco.py
│   ├── conta.py
│   ├── storage.py
│   └── utils.py
│
├── data/
│   └── banco_dados.json
│
├── tests/              # (Opcional)
├── README.md
├── LICENSE
├── .gitignore
├── .gitattributes
└── run.py
```

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/sistema_bancario.git
cd sistema_bancario
```

### 2. Execute o projeto

```bash
python run.py
```

Ou:

```bash
python -m src.main
```

---

## 🧭 Menu do sistema

```
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
```

---

## 💾 Persistência de dados

* Os dados são salvos automaticamente em:

  ```
  data/banco_dados.json
  ```

* O salvamento ocorre após:

  * Criar conta
  * Depositar
  * Sacar
  * Transferir

* Ao iniciar o sistema:

  * O arquivo JSON é carregado automaticamente (se existir)

* O JSON é legível e pode ser editado manualmente ⚠️ (com cuidado)

---

## 🔧 Requisitos

* Python 3.10 ou superior
  *(testado com Python 3.12)*

---

## 🐛 Possíveis problemas e soluções

| Problema                                  | Solução                                                                               |
| ----------------------------------------- | ------------------------------------------------------------------------------------- |
| `KeyError: 'historico'` ao carregar dados | JSON antigo. Apague `data/banco_dados.json` ou adicione `"historico": []` manualmente |
| Valores negativos em operações            | O sistema bloqueia automaticamente e exibe erro                                       |

---

## 📝 Licença

Este projeto está sob a licença **MIT**.
Consulte o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

**Samuel Lisboa**
GitHub: @lisboasamuu

---

## 📌 Melhorias futuras

* Limite de transferências por dia
* Geração de extrato em PDF
* Interface gráfica (Tkinter ou PyQt)
* Tipos de conta (corrente/poupança)
* Autenticação por senha

---

## 🧠 Observação técnica

Esse projeto já demonstra:

* Separação de responsabilidades (Banco vs Conta vs Storage)
* Persistência desacoplada
* Estrutura modular (nível de projeto real)

Com pequenos upgrades, isso vira facilmente um **backend de API bancária**.

---
