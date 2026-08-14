flag = 1

while flag != 3:
    try:
        while flag == 1:
            notaA = float(input("Qual a sua primeira nota?"))
            if 0 <= notaA > 10:
                notaA = float(input("Nota inválida, Qual a sua primeira nota?"))
            flag = 2

        while flag == 2:
            notaB = float(input("Qual a sua segunda nota?"))
            if 0 <= notaB > 10:
                notaB = float(input("Nota inválida, Qual a sua segunda nota?"))
            flag = 3
    except ValueError:
        print("Insira um numero!!!!!!!")


media = (notaA + notaB) / 2
print(f"A sua media é {media}")
