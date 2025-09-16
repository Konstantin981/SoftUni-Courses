n = int(input())
odd_sum = 0
even_sum = 0

for idx in range(1, n+1):
    new_number = int(input())

    if idx%2 == 0:
        even_sum+= new_number

    else:
        odd_sum += new_number

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
     print("No")
     print(f"Diff = {abs(even_sum-odd_sum)}")