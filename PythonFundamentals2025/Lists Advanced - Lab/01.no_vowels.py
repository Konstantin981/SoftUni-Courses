text = input()
sorted_text = [char for char in text if char.lower() not in ('a', 'e', 'i', 'o', 'u', 'a')]
print(''.join(sorted_text))