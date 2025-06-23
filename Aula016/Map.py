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

