player_name = input()
points_remaining = 301
unsuccessful_shots = 0
successful_shots = 0

while True:
    zone = input()
    if zone == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    points_scored = int(input())
    if zone == "Double":
        points_scored *= 2
    elif zone == "Triple":
        points_scored *= 3

    if points_scored > points_remaining:
        unsuccessful_shots += 1

    elif points_scored < points_remaining:
        successful_shots += 1
        points_remaining -= points_scored

    elif points_scored == points_remaining:
        successful_shots += 1
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break