N1 = int(input())
N2 = int(input())
operation = input()
result = ""

if operation  == "+":
    result = (f"{N1} {operation} {N2} = {N1 + N2}"
              f"{' - even' if (N1+N2)%2==0 else ' - odd'}")
elif operation == "-":
    result = (f"{N1} {operation} {N2} = {N1 - N2}"
              f"{' - even' if (N1 - N2) % 2 == 0 else ' - odd'}")
elif operation == "*":
    result = (f"{N1} {operation} {N2} = {N1 * N2}"
              f"{' - even' if (N1 * N2) % 2 == 0 else ' - odd'}")
elif operation == "/":
    if not(N2==0):
        result = (f"{N1} / {N2} = {(N1/N2):.2f}")
    else:
        result  = (f"Cannot divide {N1} by zero")
elif operation == "%":
    if not(N2==0):
        result = (f"{N1} % {N2} = {N1%N2}")
    else:
        result = (f"Cannot divide {N1} by zero")

print (result)