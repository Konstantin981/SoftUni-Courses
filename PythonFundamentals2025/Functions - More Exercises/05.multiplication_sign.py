def is_negative(number):
    if number < 0:
        return True
    elif number == 0:
        return None
    else:
        return False
number1 = int(input())
number2 = int(input())
number3 = int(input())
counter = 0
numbers = [number1, number2, number3]
lst = list(map(is_negative, numbers))
for element in lst:
    if element:
        counter+=1
if None in lst:
    print("zero")
elif counter % 2 == 0:
    print("positive")
else:
    print("negative")