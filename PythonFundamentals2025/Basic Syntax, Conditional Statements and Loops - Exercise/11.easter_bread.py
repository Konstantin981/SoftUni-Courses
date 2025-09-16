budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
colored_eggs = 0
bread_made = 0
price_per_loaf = flour_price + eggs_price + 0.25 * milk_price

while budget > price_per_loaf:
    budget -= price_per_loaf
    bread_made += 1
    colored_eggs += 3
    if bread_made % 3 == 0:
        colored_eggs -= bread_made - 2

print(f"You made {bread_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")