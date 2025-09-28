working_day_events = input().split('|')
energy = 100
coins = 100
was_closed = False
for event in working_day_events:
    new_event = event.split('-')
    current_event, current_index = new_event[0], int(new_event[1])
    if current_event == 'rest':
        energy_before = energy
        energy += current_index
        if energy > 100:
            energy = 100
        gained_energy = energy - energy_before
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif current_event == 'order':
        if energy >= 30:
            energy -= 30
            coins += current_index
            print(f"You earned {current_index} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= current_index:
            coins -= current_index
            print(f"You bought {current_event}." )
        else:
            print(f"Closed! Cannot afford {current_event}.")
            was_closed = True
            break
if not(was_closed):
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")