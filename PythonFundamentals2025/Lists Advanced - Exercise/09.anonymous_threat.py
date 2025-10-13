strings = input().split()
while True:
    command = input()
    if command == "3:1":
        break
    command = command.split()
    if command[0]=="merge":
        start = int(command[1])
        end = int(command[2])
        start = max(0, start)
        end = min(len(strings)- 1, end)
        merged = "".join(strings[start:end + 1])
        strings[start:end + 1] = [merged]
    elif command[0]=="divide":
        portions_length = len(strings[int(command[1])]) // int(command[2])
        word = strings[int(command[1])]
        strings.remove(strings[int(command[1])])
        portion_start = 0
        portion_end = portions_length
        for i in range(int(command[2])):
            if i==int(command[2])-1:
                strings.insert(int(command[1]) + i, word[portion_start:])
            else:
                strings.insert(int(command[1]) + i, word[portion_start:portion_end])
            portion_start = portion_end
            portion_end = portion_end+portions_length
print(" ".join(strings))