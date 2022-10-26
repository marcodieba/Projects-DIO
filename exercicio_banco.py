
import time
print("""Bem Vindo Ao Perereca-Banks \nOque deseja fazer? \n menu \n D - Para Deposito \n S - Para saque\n E - Para extrato \n Q - Para Sair""")
limite_diario = 1
limite_saque = 500
iteracao = input("Digite a operação:").upper()
saldo = 0
extrato = []
while iteracao != 'Q':
    if iteracao == 'D':
        deposito = float(input("Valor do Deposito:"))
        if deposito > 0:
            saldo += deposito
            extrato.append(f"Deposito R${deposito:.2f}")
            print('Deposito realizado com sucesso!')
            operacao = input("Deseja realizar um novo deposito?:").upper()
        else:
            print("Deposito de negativo não autorizado")
            operacao = input("Deseja realizar um novo deposito?:").upper()
        if operacao == "S":
            iteracao = "D"
        else:
            iteracao = input("Digite a operação:").upper()
    elif iteracao == 'S':
        if limite_diario <= 3:
            saque = float(input("Valor a sacar:"))
            if saque <= saldo and saque <= limite_saque :
                limite_diario += 1
                saldo -= saque
                extrato.append(f"Saque R${saque:.2f}")
                print("Aguarde a contagem das notas")
                time.sleep(2)
                print("Saque realizado com sucesso!")
                operacao = input("Deseja realizar um novo saque?:").upper()
            elif saque > limite_saque:
                print("Valor Maximo por saque R$500,00")
                iteracao = "S"
            else:
                print("Saldo insuficiente")
                print("Menu Inicial")
                iteracao = input("Digite a operação:").upper()

            if operacao == "S":
                iteracao = "S"
            else:
                iteracao = input("Digite a operação:").upper()
        else:
            print("Limite de saque diario excedido")
            iteracao = input("Digite a operação:").upper()

    elif iteracao == "E":
        extrato.append(f"Saldo em conta R${saldo:.2f}")
        for obj in extrato:
            print(obj)
        iteracao = input("Digite a operação:").upper()

    else:
        print("""Favor utilizar o seguinte menu
                 D - Para Deposito
                 S - Para saque
                 E - Para extrato
                 Q - Para Sair""")
        iteracao = input("Digite a operação:").upper()

print("Obrigado por utilizar o Perereca-Banks")
