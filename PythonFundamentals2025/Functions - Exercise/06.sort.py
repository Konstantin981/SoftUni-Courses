numbers_as_strings = input().split(" ")
numbers_as_integers = []
for number in numbers_as_strings:
    numbers_as_integers.append(int(number))
sorted_numbers = sorted(numbers_as_integers)
print(sorted_numbers)