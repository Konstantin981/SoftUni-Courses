def in_between(a, b):
    lst = []
    for i in range(ord(a) + 1, ord(b)):
        lst.append(chr(i))
    return lst
char1 = input()
char2 = input()
result = in_between(char1, char2)
print(" ".join(result))