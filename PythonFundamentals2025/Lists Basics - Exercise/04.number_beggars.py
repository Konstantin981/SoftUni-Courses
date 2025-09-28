money_as_strings = input().split(', ')
number_of_beggars = int(input())
money_as_integer = []
for money in money_as_strings:
    money_as_integer.append(int(money))
beggar_sums = []
start_index = 0
for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for index in range(start_index, len(money_as_integer), number_of_beggars):
        current_beggar_sum += money_as_integer[index]
    beggar_sums.append(current_beggar_sum)
    start_index += 1

print(beggar_sums)