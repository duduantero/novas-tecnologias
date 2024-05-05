def eh_primo(numero):
  if numero == 2:
    return True
  elif numero < 2 or numero % 2 == 0:
    return False
  for i in range(3, int(numero**0.5) + 1, 2):
    if numero % i == 0:
      return False
  return True


def imprimir_n_primos(n):
  contador = 0 
  numero = 2  
  while contador < n:
    if eh_primo(numero):
      print(numero, end=' ')
      contador += 1
    numero += 1


n = int(input("Digite um número inteiro:"))
print(f"Os {n} primeiros números primos são:")
imprimir_n_primos(n)
