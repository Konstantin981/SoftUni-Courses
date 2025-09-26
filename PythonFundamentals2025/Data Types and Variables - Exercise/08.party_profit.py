group_size = int(input())
days = int(input())
coins = 0
for i in range(1,days+1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5
    if i % 3 == 0:
        coins-= group_size * 3
    if i % 5 == 0:
        coins += 20 * group_size
        if i % 3 == 0:
            coins -= group_size * 2
    coins+=50
    coins-= group_size*2
coins_per_companion = coins // group_size
print(f"{group_size} companions received {coins_per_companion} coins each.")