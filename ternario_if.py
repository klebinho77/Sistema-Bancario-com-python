saldo = 2000
saque = 500

status = "Sucess" if saldo >= saque else "Falha"

print(f"{status} ao realizar saque")