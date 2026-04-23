# 🐍 Python Avançado — Exercícios Práticos

Este repositório reúne desafios de **nível avançado em Python**, com foco em conceitos fundamentais utilizados no desenvolvimento real de software.

A proposta é ir além da sintaxe básica e trabalhar com **estrutura, organização de código e boas práticas**.

---

## 🚀 Objetivo

Desenvolver habilidades práticas em:

* Programação orientada a objetos (POO)
* Manipulação de arquivos
* Uso de decorators
* Funções de ordem superior
* Otimização com cache (memoization)
* Tratamento de erros

---

## 🧠 Exercício 1 — Mini Sistema Bancário

Implementação de um sistema bancário utilizando **classes** e persistência de dados.

### 📌 Estrutura:

* Classe `Conta`

  * `titular`
  * `saldo`
  * `historico`

* Métodos:

  * `depositar(valor)`
  * `sacar(valor)`
  * `transferir(conta_destino, valor)`

* Classe `Banco`

  * Gerencia múltiplas contas usando dicionário

---

### 💾 Persistência de Dados:

* Salvamento em arquivo (`.json` ou `.txt`)
* Carregamento automático ao iniciar o sistema

---

### 🧾 Exemplo de histórico:

```id="lq8c0g"
+100 depósito
-50 saque
-> transferência para João
```

---

## 🔄 Exercício 2 — Decorator de Log

Criação de um **decorator personalizado** para monitoramento de funções.

### 📌 Funcionalidades:

* Registrar:

  * Nome da função
  * Argumentos recebidos
  * Valor de retorno

* Armazenar logs em arquivo `log.txt`

---

### 🧪 Exemplo:

```python id="r9m3kt"
@log
def soma(a, b):
    return a + b
```

---

### 🔥 Funcionalidades extras:

* Registro de exceções (`try/except`)
* Medição de tempo de execução da função

---

## 🧩 Exercício 3 — Sistema de Cache (Memoization)

Implementação manual de um sistema de cache para otimizar chamadas de funções.

### 📌 Objetivo:

* Evitar recomputação de resultados
* Melhorar performance

---

### 🧪 Exemplo:

```python id="8drn4h"
@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

---

### 🔥 Funcionalidades extras:

* Implementação sem `functools`
* Contagem de execuções reais da função
* Comparação de performance (com vs sem cache)

---

## 🧠 Conceitos Aplicados

* Classes e objetos (`__init__`, métodos)
* Decorators
* Funções como argumento
* Estruturas de dados (listas e dicionários)
* Leitura e escrita em arquivos
* Tratamento de erros com `try/except`

---

## 😈 Desafio Extra

Integração de todos os conceitos em um único projeto:

* Sistema bancário com:

  * Logs automáticos (decorators)
  * Otimização de operações (cache)

---

## 📌 Autor

Desenvolvido por **Samuel Lisboa** 🚀

---

## 📣 Contribuição

Sinta-se à vontade para sugerir melhorias ou abrir issues!

Se curtir o projeto, considere dar uma ⭐

---
