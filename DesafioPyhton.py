menu = """

1- Depositar
2- Sacar
3- Extrato
4- Sair

=> """
limite = 500
limite_saque = 3
valor = 0
saldo = 0
extrato = ""


while True:
    opcao = input(menu)
    if opcao == "1":
        while True:
            valor = input("Qual o valor do deposito?")

            if int (valor) > 0:
                saldo += int (valor)
                extrato = f"Depósito no valor de R${valor} \n"
                break

            else:
                print ("Por favor, insira um valor válido")
                

    elif opcao == "2":
        valor = input("Qual o valor de saque?")

        if int (valor) > 0 and valor <= limite and saldo >= int(valor) and limite_saque <= 3:
            saldo -= int (valor)
            limite_saque -= 1
            extrato += f"Saque no valor de R${valor} \n"

        elif limite > 500:
            print (f"O limite de saque é {limite}")
        
        elif limite_saque > 3:
            print (f"O limite de saques diários é {limite_saque}")

        elif int (valor) > saldo:
            print (f"Saldo indisponível. \n Seu saldo é {saldo}")

        elif limite_saque > 3:
            print ("Limite de saque diário atingido")

    elif opcao == "3":
        if not extrato:
            print (f"Não foram realizadas movimentações \n Seu saldo é {saldo}")
        else:
            print(f"""
==========Extrato==========
{extrato}


Seu saldo é:R${saldo}
"""
)
    elif opcao == 4:
        break
    
    else:
        print ("Opção inválida")


        
