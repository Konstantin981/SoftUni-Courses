lst = input().split(", ")
positive_lst = [number for number in lst if int(number) >= 0]
negative_lst = [number for number in lst if int(number) < 0]
even_lst = [number for number in lst if int(number)%2 == 0]
odd_lst = [number for number in lst if int(number)%2 != 0]
print(f"Positive: ", end = "")
print(", ".join(positive_lst))
print(f"Negative: ", end = "")
print(", ".join(negative_lst))
print(f"Even: ", end="")
print(", ".join(even_lst))
print(f"Odd: ", end="")
print(", ".join(odd_lst))