n = int(input())

counter = 0
is_max_number = False
for row in range(1, n+1):
    for col in range(row):
        counter += 1
        print(counter, end=" ")
        if counter == n:
            is_max_number = True
            break

    if is_max_number:
        break
    print()