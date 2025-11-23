def cast_spell(heroes:dict, some_action:list)->dict:
    hero, mp_needed, spell_name= some_action[1], int(some_action[2]), some_action[3]
    if heroes[hero]["MP"] >= mp_needed:
        heroes[hero]["MP"] -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['MP']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")
    return heroes
def take_damage(heroes:dict, some_action:list)->dict:
    hero, damage, attacker = some_action[1],int(some_action[2]), some_action[3]
    heroes[hero]["HP"] -= damage
    if heroes[hero]["HP"] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!")
    else:
        print(f"{hero} has been killed by {attacker}!")
        del heroes[hero]
    return heroes
def recharge(heroes:dict, some_action:list)->dict:
    hero,  amount = some_action[1],int(some_action[2])
    beginning_amount = heroes[hero]["MP"]
    heroes[hero]["MP"] += amount
    if heroes[hero]["MP"]>200:
        heroes[hero]["MP"]=200
    amount_recovered = heroes[hero]["MP"]-beginning_amount
    print(f"{hero} recharged for {amount_recovered} MP!")
    return heroes
def heal(heroes:dict, some_action:list)->dict:
    hero,amount = command[1], int(command[2])
    beginning_amount = heroes[hero]["HP"]
    heroes[hero]["HP"] += amount
    if heroes[hero]["HP"] > 100:
        heroes[hero]["HP"] = 100
    amount_recovered = heroes[hero]["HP"] - beginning_amount
    print(f"{hero} healed for {amount_recovered} HP!")
    return heroes

n = int(input())
heroes_dict = {}
for i in range(n):
    hero_input = input()
    hero_name, hit_points, mana_points = hero_input.split()
    heroes_dict[hero_name] = {"HP": int(hit_points), "MP":int(mana_points)}

command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        heroes_dict = cast_spell(heroes_dict, command)
    elif action == "TakeDamage":
        heroes_dict = take_damage(heroes_dict, command)
    elif action == "Recharge":
        heroes_dict = recharge(heroes_dict, command)
    elif action == "Heal":
        heroes_dict = heal(heroes_dict, command)
    command = input()

for hero_name, points in heroes_dict.items():
    print(hero_name)
    print(f"    HP: {points['HP']}")
    print(f"    MP: {points['MP']}")