lugares_vagos = [10, 2, 1, 3, 0]

while True:
    numero_da_sala = int(input("Digite o número da sala (1 a 5, digite 0 para sair): "))
    if numero_da_sala == 0:
        break
    if 1 <= numero_da_sala <= 5:
        quantidade_solicitada = int(input("Digite a quantidade de lugares solicitados: "))
        if lugares_vagos[numero_da_sala - 1] >= quantidade_solicitada:
            lugares_vagos[numero_da_sala - 1] -= quantidade_solicitada
            print("Venda realizada com sucesso!")
        else:
            print("Não há lugares suficientes disponíveis.")
    else:
        print("Número da sala inválido.")
