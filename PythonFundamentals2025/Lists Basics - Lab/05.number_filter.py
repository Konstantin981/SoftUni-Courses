even = "even"
odd = "odd"
negative = "negative"
positive = "positive"
n = int(input())
lst = []
new_lst = []
for i in range(n):
    number = int(input())
    lst.append(number)

command = input()
for num in lst:
    COMMAND = ((command == even and num % 2==0) or
              (command == odd and num % 2!=0) or
              (command == negative and num < 0) or
              (command == positive and num >= 0))
    if COMMAND:
        new_lst.append(num)

print(new_lst)