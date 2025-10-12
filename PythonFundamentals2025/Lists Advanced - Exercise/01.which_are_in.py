substrings = input().split(", ")
lst = input().split(", ")
substrings_in_lst = []
for substring in substrings:
    ok = False
    for word in lst:
        if substring in word:
            ok = True
    if ok:
        substrings_in_lst.append(substring)
print (substrings_in_lst)