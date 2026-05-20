operacao = 1
primeiro_valor = 1
segundo_valor = 1
while operacao != 0 :

    operacao = int(input("Digite a operacao que deseja realizar: \n1 - adição \n2 - subtração \n3 - divisão \n4 - multiplicação \n0 - Sair"))

    if operacao != 0 :
        primeiro_valor = float(input("Digite o primeiro numero: "))
        if(operacao == 6):
            input("Digite a porcentagem do valor 1 que você deseja ver: ")
        else: 
            segundo_valor = float(input("Dgite o segundo numero: "))

    def subtracao(primeiro_valor,segundo_valor):
        return primeiro_valor + segundo_valor
 
    def adicao(primeiro_valor,segundo_valor):
        return primeiro_valor - segundo_valor
    
    def divisao(primeiro_valor,segundo_valor):
        return primeiro_valor / segundo_valor
    
    def multiplicacao(primeiro_valor,segundo_valor):
        return primeiro_valor * segundo_valor
    
    def exponenciacao(primeiro_valor,segundo_valor):
        return primeiro_valor ** segundo_valor
    
    def porcentagem(primeiro_valor, segundo_valor ):
        return (primeiro_valor / 100 )* segundo_valor

    match operacao:
        case 1 :
            print("Sua resposta é: " , subtracao(primeiro_valor , segundo_valor))
        case 2 : 
            print("Sua resposta é: " , adicao(primeiro_valor , segundo_valor))
        case 3 :
            print("Sua resposta é: " , divisao(primeiro_valor , segundo_valor))
        case 4 : 
            print("Sua resposta é: " , multiplicacao(primeiro_valor , segundo_valor))
        case 5 : 
            print("Sua resposta é: " , exponenciacao(primeiro_valor,segundo_valor))
        case 6 : 
            print("Sua resposta é: " , exponenciacao(primeiro_valor,segundo_valor))