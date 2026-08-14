# # OPERADORES DE ATRIBUICAO
# from sqlalchemy.sql.operators import truediv
#
# num = 15
# print(num)
#
# num = num +2
# print(num)
#
# num += 2
# print(num)
#
# # OPERADORES RELACIONAIS
# print()
# print(6 < 2)
# print(6 != 2)
#
# idade = 20
# print(idade == 20)
#
# maior_idade = idade >= 18
# print(maior_idade)
#
# #OPERADOR LOGICO
# print()
#
# verificar_email = False
# verificar_senha = True
#
# login = verificar_email and verificar_senha
# print(login)
#
# if not login:
#     print("Po cara, voce e burro...")
#
# if login:
#     print("Entrou no programa")

# Ctrl + / COMENTA TUDO

print()

# nota = 7.0
#
# if nota < 6.0:
#     print("voce foi reprovado!")
#
# else:
#     print("voce foi aprovado!")
#
# print("FIM!")

nota = 7.0

if nota <= 4.0:
    print("voce foi reprovado!")
elif nota <= 6.0 :
    print("voce esta de recuperacao!")
else:
    print("voce foi aprovado")

print("FIM!")