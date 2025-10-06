start_numbers = input().split(" ")
abs_values = []
for num in start_numbers:
    abs_values.append(abs(float(num)))
print(abs_values)