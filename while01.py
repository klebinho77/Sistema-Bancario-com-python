#opcao = input(int("Please, enter the following option :\n [1] Sacar \n [2] Extrato \n[0] Sair \n:"))
opcao = -1

while opcao != 0:
    opcao = int(input("Please, enter the following option :\n [1] Sacar \n [2] Extrato \n [0] Sair \n =>  "))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print('Obrigado por usar nosso sistema...')