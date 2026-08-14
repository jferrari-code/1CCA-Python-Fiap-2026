#Correcao

endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]




def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299




#funcao que verifica se tem 2 erros seguidos
#na lista de requisitoes (codigo https) de UM endpoint
# [200, 200, 200, 200, 200] ----> false
# [201, 500, 502, 201, 500] -----> True
def erros_seguidos(requisicoes):
    for i in range(len(requisicoes) - 1):
        codigo_atual = requisicoes[i]
        prox_codigo = requisicoes[i + 1]


        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False


# [200, 200, 200, 200, 200] (requisicoes)
# [201, 500, 502, 201, 500]
def analisar_endpoint(requisicoes):
    qntd_sucessos = 0
    for codigo in requisicoes:
        if eh_sucesso(codigo):
            qntd_sucessos += 1

    qtd_total_req = len(requisicoes)
    qtd_erros = qtd_total_req - qntd_sucessos
    percentual_sucesso = (qntd_sucessos / qtd_total_req) * 100

    tem_erros_seguidos = erros_seguidos(requisicoes)

    if tem_erros_seguidos:
        classificacao = "CRITICO"
    elif percentual_sucesso >= 80:
        classificacao = "ESTAVEL"
    else:
        classificacao = "INSTAVEL"

    return (qntd_sucessos, qtd_erros, percentual_sucesso, classificacao)





# PERCORRENDO TODA A MATRIZ
qntd_maior_erro = -1
endpoint_maior_erro = ""



for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    requisicoes_endpoints = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(requisicoes_endpoints)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Requisicoes: {requisicoes_endpoints}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"Percentual: {percentual}")
    print(f"Classificacao: {classificacao}")
    print(f"-" * 30)
    print()

    if erros > qntd_maior_erro:
        qntd_maior_erro = erros
        endpoint_maior_erro = nome_endpoint

print(f"Endpoint + erros: {endpoint_maior_erro} {qntd_maior_erro}")