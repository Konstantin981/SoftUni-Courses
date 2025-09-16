from math import floor

WINER_POINTS = 2000
FINALIST_POINTS = 1200
SEMI_FINALIST_POINTS = 720

n = int(input())
starting_points = int(input())
points_made = 0
tournaments_won = 0

for i in range(1, n+1):
    result = input()
    if result == "W":
        points_made += WINER_POINTS
        tournaments_won += 1

    elif result == "F":
        points_made += FINALIST_POINTS

    elif result == "SF":
        points_made += SEMI_FINALIST_POINTS

average_points = floor(points_made/n)
win_percent = tournaments_won/n*100
final_points = starting_points + points_made

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")
