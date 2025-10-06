def rounding(lst:list):
    new_lst = []
    for item in lst:
        new_lst.append(round(item))
    print(new_lst)
lst = input().split(' ')
lst_float = []
for item in lst:
    lst_float.append(float(item))
rounding(lst_float)