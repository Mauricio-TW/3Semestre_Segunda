from cidade import Cidade
from pessoa import Pessoa
from produto import Produto
from pedido import Pedido

c1 = Cidade()
c2 = Cidade("Dublin")

p1 = Pessoa()
p2 = Pessoa("João", cid = c1)

print(p2.cidade.nome)

prod01 = Produto()
prod02 = Produto("Coca-Cola", qtd = 100)
prod03 = Produto("Pepsi", 8.99, 50)

ped01 = Pedido()
ped02 = Pedido(cli = p2)

ped02.addProd(prod03)
ped02.addProd(prod02)

print(ped02)