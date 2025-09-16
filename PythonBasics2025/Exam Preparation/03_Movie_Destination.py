film_budget = float(input())
destination = input()
season = input()
days = int(input())
price_per_day = 0

if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    elif season == "Summer":
        price_per_day = 40000
elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    elif season == "Summer":
        price_per_day = 12500
elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    elif season == "Summer":
        price_per_day = 20250

total = price_per_day * days

if destination == "Dubai":
    total = 0.7 * total
elif destination == "Sofia":
    total = 1.25 * total

if film_budget >= total:
    left = film_budget - total
    print(f"The budget for the movie is enough! We have {left:.2f} leva left!")
else:
    left = total - film_budget
    print(f"The director needs {left:.2f} leva more!")