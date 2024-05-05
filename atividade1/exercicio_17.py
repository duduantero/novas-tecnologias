def calcular_digito_verificador_e_formatar(n):
  numero_conta_str = str(n)

  s = sum(int(digito) for digito in numero_conta_str)

  d = s % 10

  numero_conta_completo = numero_conta_str.zfill(6) + '-' + str(d)

  return numero_conta_completo

n = int(input("Digite um numero de 6 digitos: "))
print(f"O número de conta completo é: {calcular_digito_verificador_e_formatar(n)}")
