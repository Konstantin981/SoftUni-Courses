schedule = input().split(", ")
while True:
    command = input()
    if command == "course start":
        break
    command = command.split(":")
    if command[0] == "Add":
        if command[1] not in schedule:
            schedule.append(command[1])
    elif command[0] == "Insert":
        if command[1] not in schedule:
            schedule.insert(int(command[2]), command[1])
    elif command[0] == "Remove":
        if command[1] in schedule:
            schedule.remove(command[1])
        if f"{command[1]}-Exercise" in schedule:
            schedule.remove(f"{command[1]}-Exercise")
    elif command[0] == "Swap":
        if command[1] in schedule and command[2] in schedule:
            index1 = schedule.index(command[1])
            index2 = schedule.index(command[2])
            if f"{command[1]}-Exercise" in schedule and f"{command[2]}-Exercise" in schedule:
                schedule[index1], schedule[index1+1], schedule[index2], schedule[index2+1] = schedule[index2], schedule[index2+1], schedule[index1], schedule[index1+1]
            elif f"{command[1]}-Exercise" in schedule and f"{command[2]}-Exercise" not in schedule:
                schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
                schedule.insert(index2+1, schedule[index1+1])
                schedule.pop(index1+1)
            elif f"{command[1]}-Exercise" not in schedule and f"{command[2]}-Exercise" in schedule:
                schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
                schedule.insert(index1+1, schedule[index2+1])
                schedule.pop(index2+2)
            else:
                schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
    elif command[0] == "Exercise":
        if command[1] in schedule and f"{command[1]}-Exercise" not in schedule:
            index = schedule.index(command[1])
            schedule.insert(index+1, f"{command[1]}-Exercise")
        elif command[1] not in schedule:
            schedule.append(command[1])
            schedule.append(f"{command[1]}-Exercise")
for i in range(len(schedule)):
    print(f"{i+1}.{schedule[i]}")