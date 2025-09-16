import sys
new_number = input()
max_number = -sys.maxsize
while new_number != "Stop":
    number = int(new_number)
    if number>max_number:
        max_number = number

    new_number = input()

print (max_number)
