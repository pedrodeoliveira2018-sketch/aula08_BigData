def venda (d,e):
    total = d * e
    # print(f'o a quantidade de itens {d} e o valor total : {total} ')
    return total


for n in range(3):
    quantidade = float(input('digite a quantidade de itens : '))
    valor = float(input('digite o valor produto  :  '))
    total = venda(quantidade,valor)
    print(f' o valor total : {total} ')