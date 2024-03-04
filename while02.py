# while True:
#     numero = int(input("informe um numero: "))
#     if numero == 10:
#         break
#     print(numero)
    
for numero1 in range(100):
    if numero1 % 2 == 0:
        continue
    
    print(numero1, end=" ")