K = int(input())
L = int(input())
M = int(input())
N = int(input())
valid_subs = 0
is_done = False

for n1 in range(K, 9):
    if is_done:
        break
    for n2 in range(9, L-1, -1):
        if is_done:
            break
        for n3 in range(M, 9):
            if is_done:
                break
            for n4 in range(9, N-1, -1):
                if n1 % 2 == 0 and n3 % 2 == 0 and n2 % 2 == 1 and n4 % 2 == 1:
                    if n1 == n3 and n2 == n4:
                        print("Cannot change the same player.")
                    else:
                        print(f"{n1}{n2} - {n3}{n4}")
                        valid_subs += 1
                    if valid_subs == 6:
                        is_done = True
                        break