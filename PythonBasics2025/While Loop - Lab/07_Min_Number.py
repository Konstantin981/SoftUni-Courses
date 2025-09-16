import sys
new_number = input()
min_number = sys.maxsize
while new_number != "Stop":
    number = int(new_number)
    if number<min_number:
        min_number = number

    new_number = input()

print (min_number)
