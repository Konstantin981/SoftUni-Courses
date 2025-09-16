degrees = int(input())
time_of_day = input()
clothing = ""
shoes = ""

if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        clothing = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon":
        clothing = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Evening":
        clothing = "Shirt"
        shoes = "Moccasins"
elif 18<degrees <= 24:
    if time_of_day == "Morning":
        clothing = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        clothing = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Evening":
        clothing = "Shirt"
        shoes = "Moccasins"
elif degrees >= 25:
    if time_of_day == "Morning":
        clothing = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        clothing = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_day == "Evening":
        clothing = "Shirt"
        shoes = "Moccasins"

print (f"It's {degrees} degrees, get your {clothing} and {shoes}.")
