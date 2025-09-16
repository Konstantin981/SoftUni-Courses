new_amount = input()
total = 0.0
while new_amount != "NoMoreMoney":
    amount = float(new_amount)
    if amount<0:
        print("Invalid operation!")
        break

    print(f"Increase: {amount:.2f}")
    total += amount
    new_amount = input()

print(f"Total: {total:.2f}")