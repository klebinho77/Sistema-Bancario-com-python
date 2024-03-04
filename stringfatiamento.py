nome = "kleber Roque Sales Aurea Kayleigh"

print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])

mensagem = f"""
Ola meu nome e {nome},
Eu estou aprendendo python.
      Essa mensagem tem diferentes recuos.
    """

print(mensagem)

curso = "Python"                                                     

print(curso[::-1])   

texto = "  Python  ".lstrip()
print(texto)

curso = "Python"                                                     

print(f"Bem vindo ao curso de {curso.upper()}!")  