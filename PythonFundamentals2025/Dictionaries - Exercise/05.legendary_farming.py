materials={
        "shards": 0,
        "fragments": 0,
        "motes": 0,
}
won_a_legendary_weapon = False
while not won_a_legendary_weapon:
    farmed = input().split()
    for i in range(0, len(farmed), 2):
        if won_a_legendary_weapon:
            break
        quantity = int(farmed[i])
        material = farmed[i+1].lower()
        if material in materials:
            materials[material] += quantity
        else:
            materials[material] = quantity
        if materials["shards"]>=250:
            print("Shadowmourne obtained!")
            materials["shards"] -= 250
            won_a_legendary_weapon = True
        elif materials["fragments"]>=250:
            print("Valanyr obtained!")
            materials["fragments"] -= 250
            won_a_legendary_weapon = True
        elif materials["motes"]>=250:
            print("Dragonwrath obtained!")
            materials["motes"] -= 250
            won_a_legendary_weapon = True

for key, value in materials.items():
    print(f"{key}: {value}")