import sys
n = int(input())
max_element = -sys.maxsize
sum = 0

for i in range(1, n+1):
    number = int(input())
    if number>max_element:
        max_element = number
    sum = sum + number

if max_element == sum - max_element:
    print("Yes")
    print(f"Sum = {sum - max_element}")
else:
    print("No")
    print(f"Diff = {abs((sum-max_element) - max_element)}")
