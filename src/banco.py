from storage import JSONStorage
from conta import Conta

class Banco:
    def __init__(self, arquivo_dados='data/banco_dados.json'):
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
