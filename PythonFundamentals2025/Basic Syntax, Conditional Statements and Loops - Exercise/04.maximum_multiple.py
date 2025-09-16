divisor = int(input())
maxi = int(input())
number = 0
for i in range(maxi, 0, -1):
    if i%divisor == 0 and i != 0:
        number = i
        break

print(number)