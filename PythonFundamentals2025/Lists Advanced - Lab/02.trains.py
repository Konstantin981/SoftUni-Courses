train = [0] * int(input())
while True:
    command = input().split(" ")
    if command[0] == "End":
        break
    elif command[0] == "add":
        train[-1]+=int(command[1])
    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people
print(train)