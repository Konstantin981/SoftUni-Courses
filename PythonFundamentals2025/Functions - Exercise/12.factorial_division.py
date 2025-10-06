def factorials(num1, num2):
    factorial1 = 1
    factorial2 = 1
    for i in range(1, num1+1):
        factorial1 = factorial1 * i
    for i in range(1, num2+1):
        factorial2 = factorial2 * i
    result = factorial1 / factorial2
    print(f"{result:.2f}")
number1 = int(input())
number2 = int(input())
factorials(number1, number2)