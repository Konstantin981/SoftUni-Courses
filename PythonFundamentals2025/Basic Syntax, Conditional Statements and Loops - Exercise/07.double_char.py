while True:
    string = input()
    if string == "End":
        break
    if string == "SoftUni":
        continue
    else:
        for i in range(len(string)-1):
            print(string[i] * 2, end="")
        print(string[len(string)-1] * 2)