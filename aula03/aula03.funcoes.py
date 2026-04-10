#So executa, nao retorna. Nao tem parametro
def print_lyrics():
    print("I ain't gonna forever")
    print("I just wanna to live while I'am alive")

print_lyrics()

print() #Pular uma linha

#So executa, nao retorna. Tem parametro
def boas_vindas(nome):
    print(f"ola {nome}, seja bem vindo(a)!")

nome_digitado = input("Digite seu nome!")
boas_vindas(nome_digitado)


#Tem parametro, retorna e executa
def soma(num_1 , num_2):
    soma = num_1 + num_2
    return soma

soma(34 , 78)
print(soma(34,78))

resultado = soma(34 , 78)
print(resultado)
print(type(nome_digitado))