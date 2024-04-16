menu = '''
    =====================
    =    [1] Depositar  =
    =    [2] Sacar      =
    =    [3] Extrato    =
    =    [0] Sair       =
    =====================
'''

saldo = 0.0
limite = 600.00
extrato = ""
total_saques = 0
limite_saques = 4

while (True):
    
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Qual o valor desejado para deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} reais \n"
        else:
            print("Operação não realizada,saldo informado inválido!")
        
    elif opcao == "2":
        valor = float(input("Qual o valor desejado para saque: "))
        
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saques_excedidos = total_saques >= limite_saques
        
        if saldo_excedido:
            print("Saldo insuficiente para realizar a transação!")
        elif limite_excedido:
            print("Valor excede o limite diário,tente outro valor!")
        elif saques_excedidos:
            print("Números de saques diários realizados!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f} reais \n"
            total_saques +=  1
        else:
            print("Operação não realizada,saldo informado inválido!")
            
    elif opcao == "3":
        print("\n==========EXTRATO==========")
        print("Nenhuma movimentação realizada!" if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f} reais")
        print("===========================")
        
    elif opcao == "0":
        break
    
    else:
        print("Operação não realizada,escolha novamente uma opção!")
    