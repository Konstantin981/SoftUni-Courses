def loot(current_treasure_chest: list, items: list)-> list:
    for item in items:
        if item not in current_treasure_chest:
            current_treasure_chest.insert(0, item)
    return current_treasure_chest

def drop(current_treasure_chest: list, index: int)-> list:
    if index in range(len(current_treasure_chest)):
        # removed_item = current_treasure_chest[current_index]
        # current_treasure_chest.pop(current_index)
        # current_treasure_chest.append(removed_item)
        current_treasure_chest.append(current_treasure_chest.pop(index))
    return current_treasure_chest
def steal(current_treasure_chest: list, count: int)-> list:
    if count >= len(current_treasure_chest):
        print(", ".join(current_treasure_chest))
        current_treasure_chest = []
    else:
        stealing_index = len(current_treasure_chest) - count
        print(", ".join(current_treasure_chest[stealing_index:]))
        current_treasure_chest = current_treasure_chest[:stealing_index]
    return current_treasure_chest
treasure_chest = input().split("|")
while True:
    command = input().split()
    action = command[0]
    if action == "Yohoho!":
        break
    if action == "Loot":
        items = command[1:]
        treasure_chest = (treasure_chest, items)
    elif action == "Drop":
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)
    elif action == "Steal":
        count = int(command[1])
        treasure_chest = steal(treasure_chest, count)
if treasure_chest == []:
    print("Failed treasure hunt.")
else:
    print(", ".join(treasure_chest))
    average_treasure_gain = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_treasure_gain} pirate credits.")