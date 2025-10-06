def is_even(number: int) ->bool:
    return number % 2 == 0
numbers_as_string = input().split(' ')
numbers_as_integers = []
for number in numbers_as_string:
    numbers_as_integers.append(int(number))
result = list(filter(is_even, numbers_as_integers))
print(result)