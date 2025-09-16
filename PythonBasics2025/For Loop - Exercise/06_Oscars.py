NOMINEE_POINTS = 1250.5

actor_name = input()
academia_points = float(input())
n = int(input())

nominated = False
for i in range(1, n+1):
    judge_name = input()
    points_given = float(input())
    academia_points += points_given * len(judge_name)/2
    if NOMINEE_POINTS < academia_points:
        nominated = True
        break

if nominated == False:
    print(f"Sorry, {actor_name} you need {(NOMINEE_POINTS-academia_points):.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academia_points:.1f}!")