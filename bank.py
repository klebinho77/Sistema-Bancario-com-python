conta_normal = False
conta_universitaria = True

saldo = int(input(('Qual e o seu saldo: ')))
saque = int(input(('Qual e o seu valor so saque? ')))

cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Sauqe realizado com uso do cheque especial")
    else:
        print('Nao foi possivle realizar o saque, saldo insuficiente')
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
else:
    print('Sistema nao reconheceu seu tipo de conta, entre em contato com o seu gerente')