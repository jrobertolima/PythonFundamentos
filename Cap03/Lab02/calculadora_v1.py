# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!
def soma(op1, op2):
    print("\nO resultado da soma é: " + str(op1+op2))

def subtrai(op1, op2):
    print("\nO resultado subtração é: " + str(op1 - op2))

def divide(op1, op2):
    print("\nO resultado divisão é: " + str(op1/op2))

def multiplica(op1, op2):
    print("\nO resultado da multiplicação é: " + str(op1*op2))

print("\n******************* Python Calculator *******************")

print("\n+++++ Escolha uma das opções abaixo +++++ ")
print("1 - Soma\n")
print("2 - Subtração\n")
print("3 - Divisão\n")
print("4 - Multiplicação\n")
print("5 - Sair\n")

#Receber a opção do usuário
op = input("\nDigite a operação a realizar: ")

while op != '5':
    #Caso escolha opção diferente do menu
    if op not in ['1', '2', '3', '4']:
        print("\nPor favor informe uma das opções do menu.")
        op = input("\nDigite a operação a realizar: ")
        continue

    #Recebendo os números com que resolver a operação
    operador1 = int(input("\nInforme o primeiro número: "))
    operador2 = int(input("\nInforme o segundo número: "))

    if op == '1':
        '''
         Alternativamente, poderia usar lambdas como abaixo:
            res = lambda x, y: x + y
            print("Com lambda fica "+ str(res(operador1, operador2)))
        '''    
        soma(operador1, operador2)
    elif op == '2':
        subtrai(operador1, operador2)
    elif op == '3':
        divide(operador1, operador2)
    else: 
        multiplica(operador1, operador2)

    #Receber nova opção do usuário
    op = input("\nDigite a operação a realizar: ")

print("\nSaindo...")


