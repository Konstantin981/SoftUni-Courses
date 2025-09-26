number = int(input())
counter = 0
for i in range(1, number+1):
    if number % i == 0:
        counter += 1

if counter == 2:
    print(True)
else:
    print(False)