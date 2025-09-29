lst = input().split(" ")
while True:
    command = input()
    if command == "No Money":
        break
    command = command.split(" ")
    if command[0] == "No Money":
        break
    if command[0] == "OutOfStock":
        replacement = "None"
        lst = [replacement if w == command[1] else w for w in lst]
    elif command[0] == "Required":
        if int(command[2]) < len(lst) and int(command[2]) >=0:
            lst[int(command[2])] = command[1]
    else:
        lst[len(lst) - 1] = command[1]
for gift in lst:
    if gift != "None":
        print(gift, end = " ")