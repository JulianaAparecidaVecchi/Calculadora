import time
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

def exibir_menu():
    print("-----| MENU CALCULADORA |-----")
    print(f"1 - soma;\n2-  subtração;\n3 - multiplicação;\n4 - divisão;\n0 - sair")
    print(30*'-')

def entrada_operacao():
    operacao=int(input("QUAL OPERAÇÃO DESEJA FAZER? "))
    return operacao

def menu(operacao,num1,num2):

        if operacao==1:
            linha()
            print(f"O resultado da sua soma é: {soma(num1,num2):.2f} \nOperação realizada: {num1} + {num2} = {soma(num1,num2):.2f}")
            linha()

        elif operacao==2: 
            linha()
            print(f"O resultado da sua subtração é: {subtracao(num1,num2):.2f}\nOperação realizada: {num1} - {num2} = {subtracao(num1,num2):.2f}")
            linha()
        elif operacao==3: 
            linha()
            print(f"O resultado da sua multiplicação é: {multiplicacao(num1,num2):.2f}\nOperação realizada: {num1} * {num2} = {multiplicacao(num1,num2):.2f}")  
            linha()
        else : 
            while num2==0:
                print('É impossivel dividir por zero, digite os números novamente!')
                num1=float(input("DIGITE O PRIMEIRO NÚMERO: "))
                num2=float(input("DIGITE O SEGUNDO NÚMERO: "))
                linha()
                print(f"O resultado da sua divisão é: {divisao(num1,num2):.2f}\nOperação realizada: {num1} / {num2} = {divisao(num1,num2):.2f}")  
                linha()   

def pedir_numero1():
    a=float(input("DIGITE O PRIMEIRO NÚMERO: "))
    return a

def pedir_numero2(): 
    b=float(input("DIGITE O SEGUNDO NÚMERO: "))
    return b

def pausa(x):
    time.sleep(x)

def linha():
    print(60*'-')


while True:
        pausa(1)
        exibir_menu()
        operacao=entrada_operacao()
        if operacao==0:
            print("FECHANDO CALCULADORA...")
            pausa(1)
            break
        if operacao>4 or operacao<0:
            print("Opção inválida! Por favor, escolha uma operação da tabela.")
            continue
        num1=pedir_numero1()
        num2=pedir_numero2()
        menu(operacao,num1,num2)
print(30*'-')
