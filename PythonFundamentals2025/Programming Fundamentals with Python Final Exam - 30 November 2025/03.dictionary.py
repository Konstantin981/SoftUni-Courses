def Test(my_dict:dict, test_words:list):
    for test_word in test_words:
        if test_word in my_dict:
            print(f"{test_word}:")
            for definition in my_dict[test_word]:
                print(f" -{definition}")
def HandOver(my_dict:dict):
    for word in my_dict.keys():
        print(word, end = " ")

my_dict = {}
words_and_definitions = input().split(" | ")
for pair in words_and_definitions:
    pair = pair.split(": ")
    word, definition = pair[0], pair[1]
    if word not in my_dict:
        my_dict[word] = []
    my_dict[word].append(definition)
test_words = input().split(" | ")
command = input()
if command == "Test":
    Test(my_dict, test_words)
elif command == "Hand Over":
    HandOver(my_dict)
