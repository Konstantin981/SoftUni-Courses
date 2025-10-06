def is_palindrome(num) -> bool:
    for i in range(len(num)):
        if num[i] != num[len(num) - i - 1]:
            return False
    return True
lst = input().split(", ")
result = list(map(is_palindrome, lst))
for item in result:
    print(item)