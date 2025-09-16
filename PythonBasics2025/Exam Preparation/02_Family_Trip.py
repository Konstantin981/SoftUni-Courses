budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())
left = 0

if nights > 7:
    price_per_night = 0.95 * price_per_night

total = price_per_night * nights
budget_for_accomodation = budget - (percent_additional_costs/100) * budget

if total <= budget_for_accomodation:
    left = budget_for_accomodation - total
    print(f"Ivanovi will be left with {left:.2f} leva after vacation.")

else:
    left = total - budget_for_accomodation
    print(f"{left:.2f} leva needed.")