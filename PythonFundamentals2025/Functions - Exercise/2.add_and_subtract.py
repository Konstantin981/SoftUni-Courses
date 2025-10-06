def add(num1:int, num2:int):
    result = num1 + num2
    return result
def subtract(num1:int, num2:int):
    result = num1 - num2
    return result
def add_and_subtract(num1:int, num2:int, num3:int):
    added = add(num1, num2)
    final = subtract(added, num3)
    print(final)
number1 = int(input())
number2 = int(input())
number3 = int(input())
add_and_subtract(number1, number2, number3)