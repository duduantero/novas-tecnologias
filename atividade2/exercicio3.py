def verificar_parenteses(expressao):
    pilha = [] 
    for char in expressao:
        if char == "(":
            pilha.append(char)  
        elif char == ")":
            if not pilha:
                return "Erro"  
            pilha.pop()  

    if not pilha:
        return "OK" 
    else:
        return "Erro"  

# Exemplos de uso
expressoes = ["(())", "()()(()())", "(()", "())"]
for expr in expressoes:
    resultado = verificar_parenteses(expr)
    print(f"Expressão '{expr}': {resultado}")
