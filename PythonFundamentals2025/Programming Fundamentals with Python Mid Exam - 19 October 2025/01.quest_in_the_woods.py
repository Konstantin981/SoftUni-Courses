days = int(input())
adventurers = int(input())
energy = float(input())
water_per_day = float(input())
food_per_day = float(input())
is_enough = True
total_water = water_per_day * adventurers * days
total_food = food_per_day * adventurers * days

for day in range(1, days+1):
    energy_loss_for_chopping_wood = float(input())
    energy -= energy_loss_for_chopping_wood
    if energy<=0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        is_enough = False
        break
    if day%2==0:
        energy = energy*1.05
        total_water = total_water*0.70
    if day%3==0:
        energy = energy*1.10
        total_food -= total_food/adventurers
if is_enough:
    print(f"You are ready for the quest. You will be left with {energy:.2f} energy!")