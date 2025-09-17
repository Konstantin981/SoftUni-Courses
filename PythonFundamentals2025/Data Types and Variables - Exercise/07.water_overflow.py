pours = int(input())
capacity = 255
poured = 0
for i in range(pours):
    current_pour = int(input())
    if 255 - poured < current_pour:
        print("Insufficient capacity!")
        continue
    else:
        poured += current_pour
print(poured)