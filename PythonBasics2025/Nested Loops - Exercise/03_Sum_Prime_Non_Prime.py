sum_prime = 0
sum_non_prime = 0

while True:
    new_input = input()

    if new_input == "stop":
        break

    number = int(new_input)

    if number < 0:
        print("Number is negative.")
        continue

    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += number
    else:
        sum_non_prime += number


print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")