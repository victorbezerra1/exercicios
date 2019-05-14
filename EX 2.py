pessoas = []
produtos = []

def cantina():
    for i in range(8):
        name = str(input('Digite seu nome com a primeira letra maiúscula: '))
        pedido = str(input('Digite seu pedido com a primeira letra maiúscula: '))
        pessoas.append(name)
        produtos.append(pedido)

cantina()
print('Lista de pessoas: ',pessoas, '|| Seus respectivos pedidos: ', produtos)

