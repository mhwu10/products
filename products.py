products = [ ]
while True:
    name = input('what is the name of your produc: ')
    if name == 'q':
        break
    price = input('what is the price of this produc: ')
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