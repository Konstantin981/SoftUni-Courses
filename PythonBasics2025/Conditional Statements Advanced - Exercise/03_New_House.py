flower = input()
amount = int(input())
budget = int(input())
total = 0
left = 0

if flower == "Roses":
    total = amount*5
    if amount > 80:
        total = 0.9*total
elif flower == "Dahlias":
    total = amount * 3.80
    if amount > 90:
        total = 0.85 * total
elif flower == "Tulips":
    total = amount * 2.80
    if amount > 80:
        total = 0.85 * total
elif flower == "Narcissus":
    total = amount * 3
    if amount < 120:
        total = 1.15 * total
elif flower == "Gladiolus":
    total = amount * 2.50
    if amount < 80:
        total = 1.20 * total

if budget >= total:
    left = budget-total
    print(f"Hey, you have a great garden with {amount} {flower} and {left:.2f} leva left.")
else:
    left = total-budget
    print(f"Not enough money, you need {left:.2f} leva more.")