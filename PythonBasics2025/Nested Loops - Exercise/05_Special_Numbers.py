n = int(input())
result = ""
for number in range(1111, 10000):
    is_special = True
    for num in str(number):
        if num == "0":
            is_special = False
            break
        if n % int(num) != 0:
            is_special = False

    if is_special:
        result += str(number) + " "

print(result)