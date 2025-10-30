bakery = {}
command = input()
while command != "statistics":
    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])
    if product in bakery:
        bakery[product]+=quantity
    else:
        bakery[product] = quantity
    command = input()

print("Products in stock:")
for key in bakery.keys():
    print(f"- {key}: {bakery[key]}")
print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")