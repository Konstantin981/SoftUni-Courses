CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGAN_MENU = 8.15
DELIVERY = 2.50

num_chicken = int(input())
num_fish = int(input())
num_vegan = int(input())

total=((num_fish * FISH_MENU) + (num_chicken*CHICKEN_MENU) + (num_vegan*VEGAN_MENU))*1.2 + DELIVERY
print (total)