
def soma(a,b):
    soma_resultado= a + b
    return soma_resultado

def subtracao(a,b):
    sub_resultado= a - b 
    return sub_resultado

def multiplicacao(a,b):
    mul_resultado= a * b
    return mul_resultado

def divisao(a,b):
    div_resultado= a / b 
    return div_resultado


while True:
    print("-----| MENU CALCULADORA |-----")
    print(f"1 - soma;\n2-  subtração;\n3 - multiplicação;\n4 - divisão;\n0 - sair")
    print(30*'-')
    print
    operacao=int(input("QUAL OPERAÇÃO DESEJA FAZER? "))
    if operacao==0:
        print("FECHANDO CALCULADORA...")
        break
    if operacao>4 or operacao<0:
        print("Opção inválida! Por favor, escolha uma operação da tabela.")
        continue 
    num1=float(input("DIGITE O PRIMEIRO NÚMERO: "))
    num2=float(input("DIGITE O SEGUNDO NÚMERO: "))
    if operacao==1:
        print(f"O resultado da sua soma é: {soma(num1,num2):.2f} \nOperação realizada: {num1} + {num2} = {soma(num1,num2):.2f}")
    elif operacao==2: 
        print(f"O resultado da sua subtração é: {subtracao(num1,num2):.2f}\nOperação realizada: {num1} - {num2} = {subtracao(num1,num2):.2f}")
    elif operacao==3: 
        print(f"O resultado da sua multiplicação é: {multiplicacao(num1,num2):.2f}\nOperação realizada: {num1} * {num2} = {multiplicacao(num1,num2):.2f}")   
    else : 
        print(f"O resultado da sua divisão é: {divisao(num1,num2):.2f}\nOperação realizada: {num1} / {num2} = {divisao(num1,num2):.2f}")
 
print(30*'-')
