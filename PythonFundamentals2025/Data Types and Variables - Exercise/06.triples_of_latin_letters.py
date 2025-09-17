N = int(input())
for i in range(0, N):
    for j in range(0, N):
        for k in range(0, N):
            print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")