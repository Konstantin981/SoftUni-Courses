string = input()
for index in range(len(string)):
    if string[index] == ":":
        if index != len(string)-1:
            print(f":{string[index+1]}")