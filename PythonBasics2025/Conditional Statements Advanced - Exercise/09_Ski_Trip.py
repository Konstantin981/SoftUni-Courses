ROOM_FOR_ONE_PERSON_PRICE = 18.00
APARTMENT_PRICE = 25.00
PRESIDENT_APARTMENT_PRICE = 35.00

APARTMENT_DISC_UNDER10 = 0.3
APARTMENT_DISC_10_TO_15 = 0.35
APARTMENT_DISC_OVER_15 = 0.5

PRESIDENT_APARTMENT_DISC_UNDER10 = 0.1
PRESIDENT_APARTMENT_DISC_10_TO_15 = 0.15
PRESIDENT_APARTMENT_DISC_OVER_15 = 0.2

POSITIVE_MARK_BONUS = 0.25
NEGATIVE_MARK_BONUS = 0.1

days = int(input())
room = input()
mark = input()

total = 0

if room == "room for one person":
    total = (days-1) * ROOM_FOR_ONE_PERSON_PRICE

elif room == "apartment":
    total = (days-1) * APARTMENT_PRICE
    if days<10:
        total -= (total*APARTMENT_DISC_UNDER10)

    elif 10<=days<=15:
        total -= (total*APARTMENT_DISC_10_TO_15)

    elif days>15:
        total -= (total*APARTMENT_DISC_OVER_15)

elif room == "president apartment":
    total = (days-1) * PRESIDENT_APARTMENT_PRICE
    if days<10:
        total -= (total*PRESIDENT_APARTMENT_DISC_UNDER10)

    elif 10<=days<=15:
        total -= (total*PRESIDENT_APARTMENT_DISC_10_TO_15)

    elif days>15:
        total -= (total*PRESIDENT_APARTMENT_DISC_OVER_15)

if mark == "positive":
    total += (total*POSITIVE_MARK_BONUS)
else:
    total -= (total*NEGATIVE_MARK_BONUS)

print(f"{total:.2f}")