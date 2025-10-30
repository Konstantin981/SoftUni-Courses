products = input().split()
products_dict = {}
for i in range(0, len(products), 2):
    key = products[i]
    value = int(products[i+1])
    products_dict[key] = value

products_to_search = input().split()
for product in products_to_search:
    if product in products_dict:
        print(f"We have {products_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")