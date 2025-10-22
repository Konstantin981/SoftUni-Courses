travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for command in travel_route:
    command = command.split()
    action = command[0]
    if action == "Travel":
        distance = int(command[1])
        if distance <= fuel:
            fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            break
    elif action == "Enemy":
        armour = int(command[1])
        if ammunition >= armour:
            ammunition -= armour
            print(f"An enemy with {armour} armour is defeated." )
        elif fuel >= armour*2:
            fuel -= armour*2
            print(f"An enemy with {armour} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif action == "Repair":
        amount = int(command[1])
        fuel += amount
        ammunition += amount*2
        print(f"Ammunitions added: {amount*2}." )
        print(f"Fuel added: {amount}.")
    elif action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break