start = input()
end = input()

s1 = int(start[0])
s2 = int(start[1])
s3 = int(start[2])
s4 = int(start[3])

e1 = int(end[0])
e2 = int(end[1])
e3 = int(end[2])
e4 = int(end[3])

is_odd = False

for n1 in range(s1, e1+1):
    for n2 in range(s2, e2+1):
        for n3 in range(s3, e3+1):
            for n4 in range(s4, e4+1):
                if n1%2 == 1 and n2%2 == 1 and n3%2 == 1 and n4%2 == 1:
                    print(f"{n1}{n2}{n3}{n4}", end = ' ')
