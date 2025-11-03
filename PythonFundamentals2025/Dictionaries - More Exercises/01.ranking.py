contests = {}
contest_points = {}
max_sum = 0
best_candidate = ""
command = input()
while command != "end of contests":
    command = command.split(":")
    contest = command[0]
    password = command[1]
    contests[contest] = password
    command = input()

command = input()
while command != "end of submissions":
    command = command.split("=>")
    contest = command[0]
    password = command[1]
    username = command[2]
    points = int(command[3])
    if contest in contests and password == contests[contest]:
        if username not in contest_points:
            contest_points[username] = {}
        if contest not in contest_points[username]:
            contest_points[username][contest] = points
        else:
            if points > contest_points[username][contest]:
                contest_points[username][contest] = points

    command = input()

for user, all_scores in contest_points.items():
    current_sum = sum(all_scores.values())
    if current_sum > max_sum:
        max_sum = current_sum
        best_candidate = user
for user in contest_points:
    contest_points[user] = dict(
        sorted(contest_points[user].items(), key=lambda x: -x[1])
    )
contest_points = dict(sorted(contest_points.items()))
print(f"Best candidate is {best_candidate} with total {max_sum} points.")
print("Ranking:")
for user, all_scores in contest_points.items():
    print(user)
    for key,value in all_scores.items():
        print(f"#  {key} -> {value}")