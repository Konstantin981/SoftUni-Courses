puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

excursion_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

sum = puzzles*puzzle_price + dolls*doll_price + bears*bear_price + minions*minion_price + trucks*truck_price

if puzzles+dolls+bears+minions+trucks>=50:
    sum=sum*0.75

money_made=sum*0.9
if money_made>=excursion_price:
    left=money_made-excursion_price
    print(f"Yes! {left:.2f} lv left.")
else:
    left = excursion_price-money_made
    print(f"Not enough money! {left:.2f} lv needed.")