def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Digite um inteiro não negativo: "))


if n >= 0:
    print(f"O fatorial de {n} é {fatorial(n)}.")
else:
    print("Por favor, digite um número inteiro não negativo.")
