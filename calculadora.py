print("-----| MENU CALCULADORA |-----")
print(f"1 - soma;\n2-  subtração;\n3 - multiplicação;\n4 - divisão;\n0 - sair")
while True:
    operacao=int(input("QUAL OPERAÇÃO DESEJA FAZER? "))
    if operacao==0:
        print("FECHANDO CALCULADORA...")
        break
    num1=float(input("DIGITE O PRIMEIRO NÚMERO: "))
    num2=float(input("DIGITE O SEGUNDO NÚMERO: "))
    if operacao==1:
        soma=num1+num2
        print(f"O resultado da sua soma é: {soma:.2f} \nOperação realizada: {num1} + {num2} = {soma:.2f}")
    elif operacao==2: 
        subtracao = num1-num2
        print(f"O resultado da sua subtração é: {subtracao:.2f}\nOperação realizada: {num1} - {num2} = {subtracao:.2f}")
    elif operacao==3: 
        multiplicacao = num1*num2
        print(f"O resultado da sua multiplicação é: {multiplicacao:.2f}\nOperação realizada: {num1} * {num2} = {multiplicacao:.2f}")   
    elif operacao==4: 
        divisao = num1/num2
        print(f"O resultado da sua divisão é: {divisao:.2f}\nOperação realizada: {num1} / {num2} = {divisao:.2f}")
    else: 
        exit(print("Opção inválida! Por favor, escolha uma outra operação."))
        continue 
print("--------------------------------")    
