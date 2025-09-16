change = float(input())
change = change*100
coins_count = 0
while True:
    if change >= 200:
        change -= 200
        coins_count += 1

    elif change >= 100:
        change -= 100
        coins_count += 1

    elif change >= 50:
        change -= 50
        coins_count += 1

    elif change >= 20:
        change -= 20
        coins_count += 1

    elif change >= 10:
        change -= 10
        coins_count += 1

    elif change >= 5:
        change -= 5
        coins_count += 1

    elif change >= 2:
        change -= 2
        coins_count += 1

    elif change >= 1:
        change -= 1
        coins_count += 1

    else:
        print(coins_count)
        break

