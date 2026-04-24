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
        print('Deposito realizado com sucesso.')
        self.historico.append(f'Depósito de +R${valor:,.2f} realizado')
        return True

    def saque(self, valor):

        if valor <= 0:
            print('Ops, o valor não pode ser negativo!')
            return False
        if valor > self.saldo:
            print('Saldo insuficiente')
            return False
        self.saldo -= valor
        print('Saque realizado com sucesso.')
        self.historico.append(f'Saque de -{valor:,.2f} realizado')
        return True


    def exibir_historico(self):
        print(f'Historico de {self.titular}:')
        for operacao in self.historico:
            print(f' {operacao}')

    def exibir_saldo(self):
        print(f'Saldo de {self.titular}: R$ {self.saldo:,.2f}')

    def to_dict(self):
        '''Converte conta para um dicionario serializavel em json'''
        return {
            "titular": self.titular,
            "saldo": self.saldo,
            "historico": self.historico
        }
    @classmethod     #transforma o metodo para que ele receba a classe inteira como argumento, ao inves da self
    def from_dict(cls, data):
        #reconstruindo o objeto Conta a partir do dict criado
        conta = cls(data['titular']) #cria a conta a partir do dicionario
        conta.saldo = data.get("saldo", 0.0)
        conta.historico = data.get("historico", [])
        return conta