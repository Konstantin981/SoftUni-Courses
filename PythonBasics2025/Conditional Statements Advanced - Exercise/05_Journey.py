budget = float(input())
season = input()
destination = ""
paid = 0
accomodation = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        paid = budget * 0.3
        accomodation = "Camp"
    elif season == "winter":
        paid = budget * 0.7
        accomodation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        paid = budget * 0.4
        accomodation = "Camp"
    elif season == "winter":
        paid = budget * 0.8
        accomodation = "Hotel"
elif budget>1000:
    destination = "Europe"
    paid = budget * 0.9
    accomodation = "Hotel"

print (f"Somewhere in {destination}")
print(f"{accomodation} - {paid:.2f}")