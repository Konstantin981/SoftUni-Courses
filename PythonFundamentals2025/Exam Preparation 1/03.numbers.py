import sys

numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
biggest = [number for number in numbers if number>average]
biggest.sort(reverse=True)
if biggest == []:
    print("No")
    sys.exit()
if len(biggest)<5:
    limit = len(biggest)
else:
    limit = 5
for i in range(limit):
    print(biggest[i], end = " ")