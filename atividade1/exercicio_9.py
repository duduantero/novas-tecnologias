def imprimir_tabuada(operacao, numero):
    for i in range(1, 11):
        if operacao == 'adição':
            print(f"{numero} + {i} = {numero + i}")
        elif operacao == 'subtração':
            print(f"{numero} - {i} = {numero - i}")
        elif operacao == 'divisão':
            print(f"{numero} / {i} = {numero / i}")
        elif operacao == 'multiplicação':
            print(f"{numero} * {i} = {numero * i}")

while True:
    # Exibindo o menu de opções
    print("\nMenu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")
    print("5. Sair")
    
    # Solicitando a escolha do usuário
    escolha = input("Escolha uma operação (1-5): ")
    
    # Executando a ação com base na escolha
    if escolha == '5':
        print("Saindo do programa...")
        break
    else:
        numero = int(input("Digite um número para ver a tabuada: "))
        if escolha == '1':
            imprimir_tabuada('adição', numero)
        elif escolha == '2':
            imprimir_tabuada('subtração', numero)
        elif escolha == '3':
            imprimir_tabuada('divisão', numero)
        elif escolha == '4':
            imprimir_tabuada('multiplicação', numero)
        else:
            print("Opção inválida!")
