days = int(input())
total_food = float(input())
food_eaten_by_dog = 0
food_eaten_by_cat = 0
treats = 0

for i in range(1, days+1):
    dog = int(input())
    cat = int(input())
    if i%3 == 0:
        treats += (dog+cat) * 0.1

    food_eaten_by_dog += dog
    food_eaten_by_cat += cat

print(f"Total eaten biscuits: {treats:.0f}gr.")
food_eaten = food_eaten_by_dog + food_eaten_by_cat
percent_food= (food_eaten/total_food)*100
print(f"{percent_food:.2f}% of the food has been eaten.")
percent_dog = food_eaten_by_dog/food_eaten*100
percent_cat = food_eaten_by_cat/food_eaten*100
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")