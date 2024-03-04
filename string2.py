nome = "Kleber"
idade = 46
profissao = "Python developer"
linguagem="Python"

dados = {"nome" : "Kleber", "idade": 46}

saldo = 45.435

# print(f"Ola, me chamo {nome}. Eu tenho {idade}, trabalho como {profissao} e estou matricula no curso {linguagem}")
# print("Ola, me chamo %s. Eu tenho %d, trabalho como %s e estou matricula no curso %s" %(nome, idade, profissao, linguagem))

# PI = 3.141592

# print(f"Valor do PI : {PI:2f}")
# print(f"Valor de PI: {PI:10.2f}")

# print(" Kayleigh I love you " * 2000)

print("Nome: {nome} Idade {idade}".format(nome=nome, idade=idade))
print("Nome: {1} Idade: {0} Nome: {0} idade: {1}".format(idade,nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"nome: {nome}, Idade {idade}")

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade:{idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade:{idade} Saldo: {saldo:.2f}")