result_1 = input()
result_2 = input()
result_3 = input()

matches_won = 0
matches_lost = 0
matches_drawn = 0

if result_1[0] > result_1[2]:
    matches_won += 1
elif result_1[0] == result_1[2]:
    matches_drawn += 1
else:
    matches_lost += 1

if result_2[0] > result_2[2]:
    matches_won += 1
elif result_2[0] == result_2[2]:
    matches_drawn += 1
else:
    matches_lost += 1

if result_3[0] > result_3[2]:
    matches_won += 1
elif result_3[0] == result_3[2]:
    matches_drawn += 1
else:
    matches_lost += 1

print(f"Team won {matches_won} games.")
print(f"Team lost {matches_lost} games.")
print(f"Drawn games: {matches_drawn}")