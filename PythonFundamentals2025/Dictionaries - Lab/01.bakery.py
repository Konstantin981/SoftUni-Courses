products = input().split()
products_dict = {}
for i in range(0, len(products), 2):
    key = products[i]
    value = int(products[i+1])
    products_dict[key] = value

print(products_dict)