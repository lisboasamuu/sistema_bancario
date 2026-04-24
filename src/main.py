from banco import Banco

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