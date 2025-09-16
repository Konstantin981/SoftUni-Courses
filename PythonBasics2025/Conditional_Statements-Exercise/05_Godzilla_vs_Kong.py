budget = float(input())
extras = int(input())
costume_price = float(input())

decor_price = 0.1*budget
costume_total = extras * costume_price
if extras>=150:
    costume_total = 0.9*costume_total

total = costume_total + decor_price
if budget>=total:
    print("Action!")
    left=budget-total
    print(f"Wingard starts filming with {left:.2f} leva left.")
else:
    print("Not enough money!")
    left=total-budget
    print(f"Wingard needs {left:.2f} leva more.")