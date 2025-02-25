class Banco:
    def __init__(self):
        self.saldo = 5000
        self.pin = '741852'
        self.historico_transacoes = []
        self.limite_credito = 2500
        
    def mostrar_saldo(self):
        print(f'\nSeu saldo em conta é de: R$ {self.saldo:.2f}')
        print(f'Seu limite de crédito é de R$ {self.limite_credito:.2f}')
                
    def saque(self):
        try:
            pin = input('Insira sua senha: ')
            if pin != self.pin:
                print(' SENHA INCORRETA!')
                return  

            valor = float(input('Digite o valor que deseja sacar: R$ '))
            
            if valor <= 0:
                print('Valor incorreto, insira novamente\n')
                return

            if valor > self.saldo:
                print('Saldo insuficiente!')
                return

            self.saldo -= valor
            print('Saque realizado com sucesso!')
            self.historico_transacoes.append(f"Saque de R$ {valor:.2f}")
            self.mostrar_saldo()

        except ValueError:
            print('Digite um valor numérico válido.')
            
    def exibir_extrato(self):
        print('\nExtrato Bancário:')
        if not self.historico_transacoes:
            print('Não há transações a serem exibidas.')
        else:
            for transacao in self.historico_transacoes:
                print(f'- {transacao}')


banco = Banco()


while True:
    opcao = input('\nEscolha a ação que deseja realizar:\n'
                  '(1) - Extrato\n'
                  '(2) - Sacar\n'
                  '(3) - Sair\n'
                  'Opção: ')

    if opcao == '1':
        banco.exibir_extrato()  
    elif opcao == '2':
        banco.saque()  
    elif opcao == '3':
        break
    else:
        print('Opção inválida, tente novamente.')
