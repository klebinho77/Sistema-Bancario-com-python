while True:
    numero = int(input("Informe um numero: "))
    
    if numero % 2 == 0:
        continue
    #nao funciona teria que trocar as posicoes
    if numero == 10:
        break
    
    print(numero)