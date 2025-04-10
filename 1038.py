preco = [4.0,4.5,5.0,2.0,1.5]

pedido = input().split()
print(pedido)
codigo = int(pedido[0])-1
quantidade = int(pedido[1])

conta = preco[codigo]*quantidade

print(f"Total: R$ {conta:.2f}")
