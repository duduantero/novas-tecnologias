def quadrado_pela_soma_de_impares(n):
    soma = 0
    ultimo_impar = -1  # Inicializando com -1 para que o primeiro ímpar adicionado seja 1
    for _ in range(n):
        ultimo_impar += 2  # Isso gera a sequência de números ímpares (1, 3, 5, ...)
        soma += ultimo_impar
    return soma


n = int(input("Digite um valor: "))
print(f"O quadrado de {n}, calculado pela soma dos primeiros números ímpares é: {quadrado_pela_soma_de_impares(n)}")
