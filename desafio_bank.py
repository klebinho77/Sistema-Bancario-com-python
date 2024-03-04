menu = """
   [d] Depositar
   [s] Sacar
   [e] Extrato
   [q] Sair 
    
=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else: 
            print("Operacao falhou! O valor informado e invalido")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numeros_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente")
        
        elif excedeu_limite:
            print("Operacao falhou! O Valor do saque excede o limite")
            
        elif excedeu_saques:
            print("Operacao falhou! Numero maximo de saques excedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saques += 1
            
        else:
            print("Operacao falhou! O valor informado e invalido")
    
    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo:  R$ {saldo:.2f}")
        print("========================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada")
    
    