text = input()
final_string = ""
unique_symbols = set()
current_text = ""
current_number = ""
for ch in text:
    if not ch.isdigit():
        if current_text and current_number:
            repeated = current_text.upper() * int(current_number)
            final_string += repeated
            unique_symbols.update(repeated)
            current_text = ""
            current_number = ""
        current_text += ch
    else:
        current_number += ch
if current_text and current_number:
    repeated = current_text.upper() * int(current_number)
    final_string += repeated
    unique_symbols.update(repeated)

print(f"Unique symbols used: {len(unique_symbols)}")
print(final_string)
