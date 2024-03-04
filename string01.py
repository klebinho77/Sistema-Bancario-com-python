curso = "Python"

# # print(curso.strip())
# # print(curso.lstrip())
# # print(curso.rstrip())

# print(curso.center(10, "#"))
# print(".".join(curso))
# print(curso + "..")
# print(curso.lstrip() + "@@@@")

menu = "Python"

print("****" + menu + "****")
print(menu.center(10, "#"))

print("-".join(menu))

for letra in menu:
    print(letra, end="*")
print()