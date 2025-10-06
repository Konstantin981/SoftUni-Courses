def tribonacci_sequence(num):
    tribonacci = 1
    tribonacci_lst = [1]
    for i in range(num):
        if i==0:
            print(tribonacci, end = " ")
            continue
        elif i==1:
            tribonacci = tribonacci_lst[i-1]
            tribonacci_lst.append(tribonacci)
            print(tribonacci, end = " ")
        elif i==2:
            tribonacci = tribonacci_lst[i - 1] + tribonacci_lst[i - 2]
            tribonacci_lst.append(tribonacci)
            print(tribonacci, end = " ")
        else:
            tribonacci = tribonacci_lst[i-3]+tribonacci_lst[i-2]+tribonacci_lst[i-1]
            tribonacci_lst.append(tribonacci)
            print(tribonacci, end = " ")
number = int(input())
tribonacci_sequence(number)