def eh_primo(numero):
    if numero == 2:
        return True
    elif numero < 2 or numero % 2 == 0:
        return False
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))

if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
