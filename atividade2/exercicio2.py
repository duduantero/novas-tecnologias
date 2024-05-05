def jogo_da_forca(palavra, chances):
    palavra_oculta = ['_' for letra in palavra]
    tentativas = 0
    acertos = 0
    
    print("Bem-vindo ao Jogo da Forca!")
    print("Palavra: " + ' '.join(palavra_oculta))
    
    while tentativas < chances and acertos < len(palavra):
        letra = input("Digite uma letra: ").lower()
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    if palavra_oculta[i] == '_': 
                        palavra_oculta[i] = letra
                        acertos += 1
                    else:
                        print("Letra já foi encontrada.")
                        break
            print("Palavra: " + ' '.join(palavra_oculta))
        else:
            tentativas += 1
            print(f"Letra não encontrada. Tentativas restantes: {chances - tentativas}")
        
        if '_' not in palavra_oculta:
            print("Parabéns, você venceu!")
            break
        
    if tentativas == chances:
        print("Você perdeu! A palavra era:", palavra)

palavra_teste = 'python'
chances_teste = 3

jogo_da_forca(palavra_teste, chances_teste)
