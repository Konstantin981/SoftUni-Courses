def smallest(num1:int, num2:int, num3:int):
    return min(num1, num2, num3)
first_number=int(input())
second_number=int(input())
third_number=int(input())
smallest_number = smallest(first_number, second_number, third_number)
print(smallest_number)