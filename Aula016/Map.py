def aumentarPreco(p):
    return p * 1.1

precos = [5, 8.5, 10, 12]

novosPrecos = map(aumentarPreco, precos)
print(list(novosPrecos))

def somar(valores):
    soma = 0
    for x in valores:
        soma += x
    return soma

somas = map(somar, ((10, 5, 3), [8, 2, 1, 5]))
print(list(somas))


def quadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]

resultado = map(quadrado, numeros)  # Aplica quadrado a cada número

print(list(resultado))  # Saída: [1, 4, 9, 16, 25]

