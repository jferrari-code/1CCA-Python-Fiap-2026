cont_prod = 0

while cont_prod < 3:
    print(f"Produto {cont_prod}")
    cont_prod += 1

# while decrescente de 4 ate 1
i = 4
while i > 4:
    print(i)
    i -=1


jogar = "Sim"
flag = 1
while jogar == "Sim":
    if flag == 1:
        print("Iniciar jogo?")
        jogar = input()
        if jogar == "Não":
            break
        flag = 0
    print("Repetir o jogo?")
    jogar = input()


