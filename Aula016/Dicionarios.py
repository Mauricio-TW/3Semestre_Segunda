carro1 = {'modelo': 'Corsa', 'Ano': 2007}
carro2 = {'modelo': 'Belina', 'Ano': 1986}
carro3 = {'modelo': 'Monza', 'Ano': 1995}

print( carro1)

carro1 ['modelo'] = 'Corsa Classic'
print (carro1)

frota = carro1, carro2

print("-----------------------------------------------------------")
print(frota)
print(frota[1])

print("-----------------------------------------------------------")
for chave, valor in carro3.items():
    print(chave, " - ", valor)



# Dicionário: coleção de pares chave: valor
dicionario = {"nome": "Ana", "idade": 25, "cidade": "Rio de Janeiro"}

print(dicionario["nome"])  # Saída: Ana

# Atualizando valor
dicionario["idade"] = 26
print(dicionario["idade"])  # Saída: 26
