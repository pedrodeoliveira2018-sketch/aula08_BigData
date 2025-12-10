vendedor = []

for n in range(1) :
    print(f'\n ------ vendedores{n+1}-----')
    nome= input('informe o nome do vendedor : ')
    vendas = []

    for i  in range(5):
        venda= float(input(f'informe o valor de sua venda {i + 1} :'))
        vendas.append(venda)

    total =   sum(vendas)
    media = sum(vendas) / len (vendas)

   
    vendedo = {
        'Vendedor' : nome,
        'vendas': vendas,
        'total': total,
        'media': media
    }

    vendedor.append(vendedo)

for vendedores in vendedor :
    
    print(f'Vendedor: {vendedores["Vendedor"]}')
    print(f'vendas: {vendedores["vendas"]}')
    print(f'Total: {vendedores["total"]}')
    print(f'Media: {vendedores["media"]}')