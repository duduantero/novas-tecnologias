def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador or \
           tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    for _ in range(9):
        imprimir_tabuleiro(tabuleiro)
        try:
            linha, coluna = map(int, input(f"Jogador {jogador_atual}, escolha a linha e a coluna (separados por espaço): ").split())
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador_atual
                if verificar_vitoria(tabuleiro, jogador_atual):
                    imprimir_tabuleiro(tabuleiro)
                    print(f"Jogador {jogador_atual} venceu!")
                    return
                jogador_atual = "O" if jogador_atual == "X" else "X"
            else:
                print("Posição já ocupada, tente novamente.")
        except (ValueError, IndexError):
            print("Entrada inválida, tente novamente com valores entre 0 e 2.")
    imprimir_tabuleiro(tabuleiro)
    print("Empate!")

jogo_da_velha()
