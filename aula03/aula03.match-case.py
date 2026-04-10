#Imagine um programa que recebe a escolha do usuario
#escolha usuario
# 0 ---> sair do programa
# 1 ---> entrar do programa
# ---> erro

escolha_usuario = 0 #ou 1 ou nenhum dos dois

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
        print("Erro")
