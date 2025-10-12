lst = input().split(" ")
new_lst = [element for element in lst if len(element)%2==0]
for element in new_lst:
    print (element)