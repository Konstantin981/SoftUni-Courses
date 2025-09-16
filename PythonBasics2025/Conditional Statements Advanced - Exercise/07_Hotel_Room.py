STUDIO_MAY_OCTOBER_PRICE = 50
STUDIO_JUNE_SEPTEMBER_PRICE = 75.20
STUDIO_JULY_AUGUST_PRICE = 76

APARTMENT_MAY_OCTOBER_PRICE = 65
APARTMENT_JUNE_SEPTEMBER_PRICE = 68.7
APARTMENT_JULY_AUGUST_PRICE = 77

STUDIO_MAY_OCTOBER_DISC_7NIGHTS = 0.05
STUDIO_MAY_OCTOBER_DISC_14NIGHTS = 0.30
STUDIO_JUNE_SEPTEMBER_DISC_14NIGHTS = 0.20
APARTMENT_DISC_14NIGHTS = 0.10

month = input()
nights = int(input())
studio_sum = 0
apartment_sum = 0

if month == "May" or month == "October":
    apartment_sum = nights * APARTMENT_MAY_OCTOBER_PRICE
    studio_sum = nights * STUDIO_MAY_OCTOBER_PRICE

    if nights > 14:
        studio_sum -= (studio_sum * STUDIO_MAY_OCTOBER_DISC_14NIGHTS)

    elif nights > 7:
        studio_sum -= (studio_sum * STUDIO_MAY_OCTOBER_DISC_7NIGHTS)

elif month == "June" or month == "September":
    apartment_sum = nights * APARTMENT_JUNE_SEPTEMBER_PRICE
    studio_sum = nights * STUDIO_JUNE_SEPTEMBER_PRICE

    if nights > 14:
        studio_sum -= (studio_sum*STUDIO_JUNE_SEPTEMBER_DISC_14NIGHTS)

elif month == "July" or month == "August":
    apartment_sum = nights * APARTMENT_JULY_AUGUST_PRICE
    studio_sum = nights * STUDIO_JULY_AUGUST_PRICE

if nights>14:
    apartment_sum -= (apartment_sum * APARTMENT_DISC_14NIGHTS)


print(f"Apartment: {apartment_sum:.2f} lv.")
print(f"Studio: {studio_sum:.2f} lv.")