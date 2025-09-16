number_one = int(input())
number_two = int(input())

for number in range(number_one, number_two + 1):
    even_sum = 0
    odd_sum = 0
    for index, value in enumerate(str(number)):

        if index % 2 == 0:
            even_sum += int(value)
        else:
            odd_sum += int(value)

    if even_sum == odd_sum:
        print(number, end = " ")