import time
print("""Bem Vindo Ao Perereca-Banks \nOque deseja fazer? \n menu \n D - Para Deposito \n S - Para saque\n E - Para extrato \n Q - Para Sair""")

# iteracao = input("Digite a operação:").upper()
saldo = 0
extrato = []
cadastro = {}
conta_corrente = {}
def op_cliente(nome, cpf, idade):
    cadastro[cpf] = {'nome':nome, 'idade':idade}
    print(cadastro)

def op_conta(cliente, banco, conta, ag):
    conta_corrente[banco] = { 'conta':conta, 'ag':ag, 'cliente':cadastro[cliente]}
    print(conta_corrente)

def op_deposito(deposito, saldo=0):
    if deposito > 0:
        saldo += deposito
        extrato.append(f"Deposito R${deposito:.2f}")
        print('Deposito realizado com sucesso!')
        return saldo
    else:
        print("Deposito de negativo não autorizado")
        
def op_saque(saldo, saque):
    limite_diario = 1
    limite_saque = 500
    if limite_diario <= 3:
        if saque <= saldo and saque <= limite_saque :
            limite_diario += 1
            saldo -= saque
            extrato.append(f"Saque R${saque:.2f}")
            print("Aguarde a contagem das notas")
            time.sleep(2)
            print("Saque realizado com sucesso!")
            return saldo
            # operacao = input("Deseja realizar um novo saque?:").upper()
        elif saque > limite_saque:
            print("Valor Maximo por saque R$500,00")
            # iteracao = "S"
        else:
            print("Saldo insuficiente")
            print("Menu Inicial")
            # iteracao = input("Digite a operação:").upper()

        # if operacao == "S":
            # iteracao = "S"
        # else:
            # iteracao = input("Digite a operação:").upper()
    else:
        print("Limite de saque diario excedido")
        # iteracao = input("Digite a operação:").upper()

def op_extrato(novo_saldo):
    # if iteracao == "E":
    extrato.append(f"Saldo em conta R${novo_saldo:.2f}")
    for obj in extrato:
        print(obj)
        # iteracao = input("Digite a operação:").upper()

    # else:
    print("""Favor utilizar o seguinte menu
                D - Para Deposito
                S - Para saque
                E - Para extrato
                Q - Para Sair""")
        # iteracao = input("Digite a operação:").upper()

# Exemplo
# op_cliente('marco', '1238', '32')
# op_conta('1238', 'Perereca Banks', '221890', '1010')
# saldo = op_deposito(100)
# novo_saldo = op_saque(saldo, 10)
# op_extrato(novo_saldo)
print("Obrigado por utilizar o Perereca-Banks")