shopping_list = {}
while True:
    command = input()
    if command == "buy":
        break
    command = command.split()
    product = command[0]
    price_per_piece = float(command[1])
    quantity = int(command[2])
    if product not in shopping_list:
        shopping_list[product] = {}
        shopping_list[product][price_per_piece] = quantity
    else:
        previous_quantity_as_lst = list(shopping_list[product].values())
        previous_quantity = previous_quantity_as_lst[0]
        shopping_list[product] = {}
        shopping_list[product][price_per_piece] = quantity + previous_quantity
for key,value in shopping_list.items():
    value_as_lst = list(value.keys())
    quantity_as_lst = list(value.values())
    value_per_piece = value_as_lst[0]
    quantity = quantity_as_lst[0]
    print(f"{key} -> {(value_per_piece*quantity):.2f}")