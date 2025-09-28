collection_of_items = input().split('|')
budget = int(input())
france_money = 150
money_spent = 0
money_made = 0
items_sold_prices = []
for item in collection_of_items:
    new_item = item.split('->')
    current_item, current_price = new_item[0], float(new_item[1])
    if budget < current_price:
        continue
    if current_item == "Clothes" and current_price <= 50.00:
        money_spent += current_price
        money_made += current_price*1.4
        budget -= current_price
        items_sold_prices.append(f"{(current_price*1.4):.2f}")
    elif current_item == "Shoes" and current_price <= 35.00:
        money_spent += current_price
        money_made += current_price * 1.4
        budget -= current_price
        items_sold_prices.append(f"{(current_price*1.4):.2f}")
    elif current_item == "Accessories" and current_price <= 20.50:
        money_spent += current_price
        money_made += current_price * 1.4
        budget -= current_price
        items_sold_prices.append(f"{(current_price*1.4):.2f}")
print(*items_sold_prices)
profit = money_made - money_spent
money_made += budget
print(f"Profit: {profit:.2f}")
if money_made > france_money:
    print("Hello, France!")
else:
    print("Not enough money.")