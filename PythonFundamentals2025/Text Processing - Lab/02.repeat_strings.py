strings = input().split()
final_string = ""
for string in strings:
    final_string += string * len(string)
print(final_string)