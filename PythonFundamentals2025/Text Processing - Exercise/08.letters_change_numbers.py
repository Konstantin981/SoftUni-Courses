strings = input().split()
total_sum = 0
for string in strings:
    first_letter = string[0]
    second_letter = string[-1]
    number = int(string[1:-1])
    if first_letter.isupper():
        number = number/(ord(first_letter)-64)
    elif first_letter.islower():
        number = number * (ord(first_letter)-96)
    if second_letter.isupper():
        number = number - (ord(second_letter) - 64)
    elif second_letter.islower():
        number = number + (ord(second_letter) - 96)
    total_sum += number
print(f"{total_sum:.2f}")