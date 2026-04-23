# 🧠 Exercício 1 — Mini Banco com Classes e Persistência

# Crie um sistema de banco com:

# 📌 Requisitos:
# Classe Conta
# atributos: titular, saldo, histórico
# Métodos:
# depositar(valor)
# sacar(valor)
# transferir(conta_destino, valor)
# extrato
# Classe Banco
# gerencia várias contas (dicionário)
# 🔥 Dificuldade extra:
# Salvar os dados em arquivo (.txt ou .json)
# Carregar os dados ao iniciar o programa

# Histórico deve registrar:

# +100 depósito
# -50 saque
# -> transferência para João
class Conta:
    def __init__(self, titular):
        self.titular = titular
        #futuramente metodo criar conta
        self.saldo = 0
        self.historico = []

    def depositar(self, valor):
        if valor <= 0:
            print('Ops, o valor não pode ser negativo!')
            return False
        self.saldo += valor
        print(f'R${self.saldo:,.2f}')
        self.historico.append(f'Depósito de +R${valor:,.2f} realizado')
        print(self.historico)
        return True

    def saque(self, valor):
        if valor <= 0:
            print('Ops, o valor não pode ser negativo!')
            return False
        if valor > self.saldo:
            print('Saldo insuficiente')
            return False
        self.saldo -= valor
        self.historico.append(f'Saque de -{valor:,.2f} realizado')
    
class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, cpf, nome):
        if cpf in self.contas:
                print(f"Já existe uma conta com o CPF {cpf}.")
                return None
        conta = Conta(nome)
        self.contas[cpf] = conta
        print(f"Conta criada com sucesso para {nome} (CPF: {cpf}).")
        return conta
    

banco = Banco()
banco.criar_conta('123.456.789-10', 'Samuel')