products = [ ]
while True:
    name = input('what is the name of your produc: ')
    if name == 'q':
        break
    price = input('what is the price of this produc: ')
    price = float(price)
    #p = []
    #p.append(name)
    #p.append(price)
    #p = [name, price]
    #products.append(p)
    products.append([name, price])
#print(products)
#print(products[0][0])

for p_line in products:
    print('The price of', p_line[0], 'is', p_line[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('product,price\n')
    f.write('產品,價錢\n')
    for p in products:
        print(p[0], p[1])
        f.write(p[0] + ',' + str(p[1]) + '\n')   