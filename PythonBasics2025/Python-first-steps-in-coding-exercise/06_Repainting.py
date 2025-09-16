PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_THINNER = 5
BAGS_PRICE=0.40

nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

paint += paint * 0.1
nylon += 2

sum_materials = (PRICE_NYLON * nylon) + (PRICE_PAINT * paint) + (PRICE_THINNER * thinner) + BAGS_PRICE
workers_price = (sum_materials * 0.3) * hours

total = sum_materials + workers_price

print(total)