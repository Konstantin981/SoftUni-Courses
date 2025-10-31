mined = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource in mined:
        mined[resource] += quantity
    else:
        mined[resource] = quantity

for key, value in mined.items():
    print(f"{key} -> {value}")