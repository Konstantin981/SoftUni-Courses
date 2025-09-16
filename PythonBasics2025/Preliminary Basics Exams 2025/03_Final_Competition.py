dancers = int(input())
points_received = float(input())
season = input()
place = input()
total = 0

if place == "Bulgaria":
    total = dancers * points_received
    if season == "summer":
        total -= total * 0.05
    elif season == "winter":
        total -= total * 0.08
elif place == "Abroad":
    total = 1.5*(dancers * points_received)
    if season == "summer":
        total -= total * 0.10
    elif season == "winter":
        total -= total * 0.15

charity_donation = 0.75 * total
total -= charity_donation
money_per_dancer = total / dancers

print(f"Charity - {charity_donation:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")