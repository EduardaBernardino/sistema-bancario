from datetime import datetime 

class Transacoes:
    def __init__(self):
        self.limite_transacoes = 5 
        self.transacoes_realizadas = []  

    def limite_de_transacoes(self):
        
        if len(self.transacoes_realizadas) >= self.limite_transacoes:
            print("Você excedeu o número de transações diárias!")
            return
        
        try:
            valor = float(input("Digite o valor que deseja transferir: R$ "))
            if valor <= 0:
                print("Valor inválido! Tente novamente.")
                return
            
            horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transacoes_realizadas.append((horario, valor))
            
            print(f"O valor de R$ {valor:.2f} foi transferido com sucesso às {horario}!")
        except ValueError:
            print("Erro! Insira um valor válido.")

    def extrato_transacoes(self):
        print("\nSEU HISTÓRICO DE TRANSAÇÕES")
        if not self.transacoes_realizadas:
            print("Não há transações a serem exibidas.")
        else: 
            for horario, valor in self.transacoes_realizadas:
                print(f"{horario} - Valor: R$ {valor:.2f}")
        print("==============================\n")


banco = Transacoes()


while True:
    opcao = input("\nEscolha a ação que deseja realizar:\n"
                  "(1) - Realizar Transação\n"
                  "(2) - Exibir Histórico de Transações\n"
                  "(3) - Sair\n"
                  "Opção: ")

    if opcao == "1":
        banco.limite_de_transacoes()
        
    elif opcao == "2":
        banco.extrato_transacoes()
        
    elif opcao == "3":
        print("Encerrando o sistema...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
