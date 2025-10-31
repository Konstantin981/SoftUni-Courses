phonebook = {}
command = input()
while not command.isdigit():
    command = command.split("-")
    person = command[0]
    number = command[1]
    phonebook[person] = number
    command = input()

n = int(command)
for i in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")