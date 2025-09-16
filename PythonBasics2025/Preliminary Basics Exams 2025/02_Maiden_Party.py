LOVE_LETTER_PRICE = 0.60
WAX_ROSE_PRICE = 7.20
KEYCHAIN_PRICE = 3.60
CARICATURE_PRICE = 18.20
LUCKY_SURPRISE_PRICE = 22
DISCOUNT = 0.35
HOSTING = 0.1

maiden_party_price = float(input())
love_letters = int(input())
wax_roses = int(input())
keychains = int(input())
caricatures = int(input())
lucky_surprises = int(input())

total_products = love_letters + wax_roses + keychains + caricatures + lucky_surprises
total = ((love_letters*LOVE_LETTER_PRICE)
         + (wax_roses * WAX_ROSE_PRICE)
         + (keychains * KEYCHAIN_PRICE)
         + (caricatures * CARICATURE_PRICE)
         + (lucky_surprises * LUCKY_SURPRISE_PRICE))

if total_products > 25:
    total -= total * DISCOUNT
total -= total * HOSTING

if total >= maiden_party_price:
    left = total - maiden_party_price
    print(f"Yes! {left:.2f} lv left.")
else:
    left = maiden_party_price - total
    print(f"Not enough money! {left:.2f} lv needed.")