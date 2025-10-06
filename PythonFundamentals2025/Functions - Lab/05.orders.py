def order_price(product, amount):
    return{
        'water': 1.00 * amount,
        'coffee': 1.50 * amount,
        'coke': 1.40 * amount,
        'snacks': 2.00 * amount
    }.get(product, "Invalid product")
product = input()
amount = int(input())
result = order_price(product, amount)
if result != "Invalid product":
    print(f"{result:.2f}") 