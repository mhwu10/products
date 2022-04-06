import os # operating system

def read_file(filename):
    products = [ ]
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '產品,價錢' in line or 'product,price' in line:
                continue
                #s = line.strip().split(',')
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# let user to input
def user_input(products):
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
    print(products)
    return products

# print the record of purchase
def print_products(products):
    for p_line in products:
        print('The price of', p_line[0], 'is', p_line[1])

# write file
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('product,price\n')
        f.write('產品,價錢\n')
        for p in products:
            print(p[0], p[1])
            f.write(p[0] + ',' + str(p[1]) + '\n') 


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('file found')
        products = read_file(filename)
    else:
        print('no file found')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)


main()