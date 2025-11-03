submissions = {}
results = {}
command = input()
while command != "exam finished":
    command = command.split("-")
    if "banned" in command:
        username = command[0]
        results.pop(username)
        command = input()
        continue
    username = command[0]
    language = command[1]
    points = int(command[2])
    if language not in submissions:
        submissions[language] = 1
    else:
        submissions[language]+=1
    if username not in results:
        results[username] = points
    else:
        if points > results[username]:
            results[username] = points
    command = input()
print("Results:")
for key, value in results.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")