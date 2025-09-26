n = int(input())
lst = []
new_lst = []
key_word = input()
for i in range(n):
    string = input()
    lst.append(string)
    if key_word in string:
        new_lst.append(string)

print(lst)
print(new_lst)
