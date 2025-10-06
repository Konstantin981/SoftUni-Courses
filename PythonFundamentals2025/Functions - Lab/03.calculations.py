def calculate(operation, num1, num2):
    return{
        'multiply' : num1 * num2,
        'divide' : num1 / num2,
        'subtract' : num1 - num2,
        'add' : num1 + num2
    }.get(operation, 'Invalid operation')
operation = input()
num1 = int(input())
num2 = int(input())
print(round(calculate(operation, num1, num2)))