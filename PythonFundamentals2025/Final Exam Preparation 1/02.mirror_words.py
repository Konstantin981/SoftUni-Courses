import re
words_string = input()
mirror_words = []
pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
matches = re.findall(pattern, words_string)
if not matches:
    print("No word pairs found!")
    print("No mirror words!")
    raise SystemExit
for match in matches:
    first_word = match[1]
    second_word = match[2]
    if first_word == second_word[::-1]:
        mirror_words.append(f"{first_word} <=> {second_word}")

print(f"{len(matches)} word pairs found!")
if mirror_words:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")