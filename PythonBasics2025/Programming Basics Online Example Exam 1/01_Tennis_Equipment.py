from math import floor
from math import ceil

tennis_racket_price = float(input())
tennis_rackets = int(input())
shoes = int(input())

shoes_price = (1/6) * tennis_racket_price

total = (tennis_rackets * tennis_racket_price) + (shoes * shoes_price)
other_equipment_price = 0.2 * total
total += other_equipment_price

price_to_be_paid_by_djokovic = (1/8)*total
price_to_be_paid_by_sponsors = (7/8)*total

print(f"Price to be paid by Djokovic {floor(price_to_be_paid_by_djokovic)}" )
print(f"Price to be paid by sponsors {ceil(price_to_be_paid_by_sponsors)}" )
