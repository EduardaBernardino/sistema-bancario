class Pessoa:
    def __init__(self):
        self.nome = " "
    
        try:
            self.nome = input("Digite o seu nome: ")
            print (f"Bem vindo {self.nome}!")
        except Exception as e: 
            print(f"Ocorreu um erro: {e}")
            

            
if __name__ == "__main__":
    p = Pessoa()
else:
    print("Ocorreu um erro, tente de novo")