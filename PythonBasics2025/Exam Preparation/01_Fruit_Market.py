strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price/2
oranges_price = 0.6 * raspberries_price
bananas_price = 0.2 * raspberries_price


total = ((strawberries_quantity*strawberries_price)
         + (raspberries_quantity*raspberries_price)
         + (bananas_quantity*bananas_price)
         + (oranges_quantity*oranges_price))

print(f"{total:.2f}")