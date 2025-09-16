age = int(input())
laundry_machine_price = float(input())
toy_price = int(input())
counter = 1
money_made = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money_made += 10*counter - 1
        counter += 1
    else:
        money_made += toy_price

if money_made >= laundry_machine_price:
    N = money_made - laundry_machine_price
    print(f"Yes! {N:.2f}")
else:
    M = laundry_machine_price - money_made
    print(f"No! {M:.2f}")
