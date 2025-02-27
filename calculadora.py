def add(a, b):
    return a + b

def subtract(a, b):  
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b



print("===============MENU====================")
print("SELECIONE A OPÇÃO DESEJADA\n:")
print("1-SOMA")
print("2-SUBTAÇÃO")
print("3-MULTIPLICAÇÃO")
print("3-DIVISÃO")

escolha = input("Digite uma opção\n")

num1 = int(input("\n DIgite o primeiro numero: "))
num2 = int(input("\n DIgite o segundo numero: "))

if escolha == "1":
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")
    
elif escolha =="2":
     print(num1, "-", num2, "=", subtract(num1, num2))
     print("\n")
     
elif escolha =="3":
     print(num1, "*", num2, "*", multiply(num1, num2))
     print("\n")

elif escolha =="4":
     print(num1, "/", num2, "=", divide(num1, num2))
     print("\n")

else:
    print("Opção inválida")