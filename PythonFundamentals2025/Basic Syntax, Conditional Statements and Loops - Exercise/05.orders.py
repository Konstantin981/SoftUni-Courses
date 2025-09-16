n = int(input())
price_per_capsule = 0
days = 0
capsules_per_day = 0
total = 0
for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if capsules_per_day<1 or capsules_per_day>2000:
        continue
    elif days < 1 or days > 31:
        continue
    elif price_per_capsule<0.01 or price_per_capsule>100:
        continue
    price_today = price_per_capsule * days * capsules_per_day
    total = total + price_today
    print(f"The price for the coffee is: ${price_today:.2f}")

print(f"Total: ${total:.2f}")