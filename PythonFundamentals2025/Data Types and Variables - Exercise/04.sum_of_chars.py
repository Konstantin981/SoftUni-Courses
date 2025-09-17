N = int(input())
sum = 0
for i in range(N):
    char = input()
    sum += ord(char)
print(f"The sum equals: {sum}")