numero = input("Digite um número consistindo em cinco dígitos: ")

if len(numero) == 5 and numero.isdigit():
    digitos_separados = '   '.join(numero)
    print(digitos_separados)
else:
    print("Erro: Você deve inserir exatamente cinco dígitos.")
