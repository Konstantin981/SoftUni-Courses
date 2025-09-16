budget = int(input())
season = input()
fishermen = int(input())
boat_price = 0
left = 0

if season == "Spring":
    boat_price = 3000
    if fishermen <= 6:
        boat_price = 0.9 * boat_price
    elif 7 < fishermen <= 11:
        boat_price = 0.85 * boat_price
    elif fishermen > 12:
        boat_price = 0.75 * boat_price
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
    if fishermen <= 6:
        boat_price = 0.9 * boat_price
    elif 7 < fishermen <= 11:
        boat_price = 0.85 * boat_price
    elif fishermen > 12:
        boat_price = 0.75 * boat_price
elif season == "Winter":
    boat_price = 2600
    if fishermen <= 6:
        boat_price = 0.9 * boat_price
    elif 7 < fishermen <= 11:
        boat_price = 0.85 * boat_price
    elif fishermen > 12:
        boat_price = 0.75 * boat_price

if season != "Autumn" and fishermen%2==0:
    boat_price = boat_price * 0.95

if budget>=boat_price:
    left = budget-boat_price
    print(f"Yes! You have {left:.2f} leva left.")
else:
    left = boat_price-budget
    print(f"Not enough money! You need {left:.2f} leva.")