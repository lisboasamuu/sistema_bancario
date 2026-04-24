import os
import json


# -----------------------------------------
# Classe JsonStorage
# -----------------------------------------
class JSONStorage:
    @staticmethod
    def save(data, filename):
        '''Salvar os dados num arquivo JSON'''
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            #metodo para serializar uma string em python para uma string em json
    @staticmethod
    def load(filename):
        '''carregar os dados e retornar none se não existir'''
        if not os.path.exists(filename):
            return None
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)

# -----------------------------------------
# Classe Conta
# -----------------------------------------
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
# -----------------------------------------
# Classe Banco
# -----------------------------------------  
class Banco:
    def __init__(self, arquivo_dados='banco_dados.json'):
        self.contas = {}
        self.arquivo_dados = arquivo_dados
        self.carregar_dados()

    def criar_conta(self, cpf, nome):
        if cpf in self.contas:
                print(f"Já existe uma conta com o CPF {cpf}.")
                return None
        conta = Conta(nome)
        self.contas[cpf] = conta
        print(f"Conta criada com sucesso para {nome} (CPF: {cpf}).")
        self.salvar_dados()
        return conta
    
    def depositar(self, cpf, valor):
        conta = self.contas.get(cpf)
        if not conta:
            print('Conta não encontrada')
            return
        conta.depositar(valor)
        self.salvar_dados()

    def saque(self, cpf, valor):
        conta = self.contas.get(cpf)
        if not conta:
            print('Conta não encontrada')
            return        
        conta.saque(valor)
        self.salvar_dados()

    def obter_conta(self, cpf):
        return self.contas.get(cpf)


    def exibir_saldo(self, cpf):
        conta = self.obter_conta(cpf)
        if conta:
            conta.exibir_saldo() 

    def exibir_historico(self, cpf):
        conta = self.obter_conta(cpf)
        if conta:
            conta.exibir_historico()

    def transferir(self, cpf_origem, cpf_destino, valor):
        modalidade = input('Qual a modalide do pagamento? ').strip()
        if modalidade == '':
            print('Informe a modalidade!')
            return False        
        #localiza as contas
        conta_origem = self.obter_conta(cpf_origem)
        if not conta_origem:
            print('Conta origem não encontrada!')
            return False

        conta_destino = self.obter_conta(cpf_destino)
        if not conta_destino:
            print('Conta destino não encontrada!')
            return False

        #validação do dado de valor
        if valor <= 0:
            print('Ops, o valor não pode ser negativo!')
            return False
        if valor > conta_origem.saldo:
            print('Saldo insuficiente')
            return False
        #realização da transferencia
        conta_origem.saldo -= valor
        conta_destino.saldo += valor
        #salvamento do dado
        self.salvar_dados()
        #adicionando ao historico
        conta_origem.historico.append(f'{modalidade} enviada para {cpf_destino} no valor de {valor}')
        conta_destino.historico.append(f'{modalidade}a recebida de {cpf_origem} no valor de {valor}')

        print(f'{modalidade} realizada com sucesso!')
        print(f'De: {conta_origem.titular} para {conta_destino.titular}')

# --- PERSISTENCIA DE DADOS 
#             
    def salvar_dados(self):
        dados = {}
        for cpf, conta in self.contas.items():
            dados[cpf] = conta.to_dict()
        JSONStorage.save(dados, self.arquivo_dados)

    def carregar_dados(self):
        dados = JSONStorage.load(self.arquivo_dados)
        if dados is None:
            print('Nenhum arquivo de dados encontrado. Iniciando banco vazio')
            return 
        self.contas = {}
        for cpf, dados_contas in dados.items():
            self.contas[cpf] = Conta.from_dict(dados_contas)
        print(f'\nDados carregados e {len(self.contas)} conta(s) restaurada(s)')

def main():
    banco = Banco()
    while True:
        print("\n" + "=" * 50)
        print("          🏦 SISTEMA BANCÁRIO LISBOA")
        print("=" * 50)
        print("1️⃣  Criar nova conta")
        print("2️⃣  Depositar")
        print("3️⃣  Sacar")
        print("4️⃣  Consultar saldo")
        print("5️⃣  Ver histórico de movimentações")
        print("6️⃣  Transferir")
        print("0️⃣  Sair")
        print("=" * 50)

        opcao = input('Escolha uma opção: ').strip()
        if opcao == '0':
            print('\nO 🏦 SISTEMA BANCÁRIO LISBOA AGRADECE!\n')
            break
        elif opcao == '1':
            cpf = input('insira seu cpf: ').strip()
            nome = input('insira seu nome: ').strip()
            banco.criar_conta(cpf, nome)
        elif opcao == '2':
            cpf = input('insira o CPF do titular: ').strip()
            valor = float(input('Insira o valor que deseja depositar: '))
            banco.depositar(cpf, valor)
        elif opcao == '3':
            cpf = input('insira seu cpf: ').strip()
            valor_saque = float(input('Insira o valor que deseja sacar: '))
            banco.saque(cpf, valor_saque)
        elif opcao == '4':
            cpf = input('insira seu cpf da conta que deseja ver o saldo: ').strip()
            banco.exibir_saldo(cpf)
        elif opcao == '5':
            cpf = input('insira seu cpf: ').strip()
            banco.exibir_historico(cpf)
        elif opcao == '6':
            cpf_origem = input('Informe o CPF da conta de origem da transferência: ')
            cpf_destinatario = input('Informe o CPF da conta de destino: ')
            valor_transferencia = float(input('Informe o valor de transferência: ').replace(",", "."))
            banco.transferir(cpf_origem, cpf_destinatario, valor_transferencia)

if __name__ == "__main__":
    main()