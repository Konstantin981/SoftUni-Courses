def perfect_number(num):
    dividers = []
    for i in range(1,num):
        if num%i==0:
            dividers.append(i)
    for divider in dividers:
        num -= divider
    if num==0:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
number = int(input())
perfect_number(number)
