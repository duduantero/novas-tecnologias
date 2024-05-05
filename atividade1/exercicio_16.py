def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1  # Os dois primeiros termos
    for _ in range(2, n):
        a, b = b, a + b  # Atualiza os valores de a e b para os próximos dois termos
    return b

# Exemplo de uso da função
n = int(input("Digite o n: "))
print(f"O {n}-ésimo termo da série de Fibonacci é: {fibonacci(n)}")
