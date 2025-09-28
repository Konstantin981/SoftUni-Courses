numbers_as_strings = input().split(' ')
numbers_to_remove = int(input())
numbers_as_integers = []
for number in numbers_as_strings:
    numbers_as_integers.append(int(number))
for i in range(numbers_to_remove):
    smallest = min(numbers_as_integers)
    numbers_as_integers.remove(smallest)
print(*numbers_as_integers, sep=', ')