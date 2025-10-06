numbers_as_strings = input().split()
numbers_as_integers = []
for number in numbers_as_strings:
    numbers_as_integers.append(int(number))
sum_num = sum(numbers_as_integers)
min_num = min(numbers_as_integers)
max_num = max(numbers_as_integers)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")