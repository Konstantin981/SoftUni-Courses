n = int(input())
synonyms = {}
for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = [synonym]
    else:
        synonyms[word].append(synonym)

for word, synonym_list in synonyms.items():
    synonym_str = ", ".join(synonym_list)
    print(f"{word} - {synonym_str}")