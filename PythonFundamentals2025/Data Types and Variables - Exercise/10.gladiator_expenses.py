lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmets_broken = lost_fights // 2
swords_broken = lost_fights // 3
shield_broken = lost_fights // 6
armor_broken = lost_fights // 12
total_price = (helmets_broken * helmet_price) \
              + (swords_broken * sword_price) \
              + (shield_broken * shield_price) \
              + (armor_broken * armor_price)
print(f"Gladiator expenses: {total_price:.2f} aureus")