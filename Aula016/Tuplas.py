def calcular(x, y):
    return x + y, x - y, x * y, x / y

result = calcular(10, 5)

print (result)

for x in result: print(x)

a, b, c, d = result
print("Soma: ", a)
print("Subtração: ", b)
print("Multiplicação: ", c)
print("Divisão: ", d)


# Tupla: coleção imutável de elementos
tupla = (1, 2, 3, 4)
print(tupla[2])  # Saída: 3

# Tuplas são imutáveis, não é possível alterar um valor
# tupla[0] = 10  # Isso causaria erro
