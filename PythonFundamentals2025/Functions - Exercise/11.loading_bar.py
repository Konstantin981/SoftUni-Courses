def loading_bar(num):
    load = "[" + (num//10)*"%" + (10-num//10)*"." + "]"
    return load
number = int(input())
loaded = loading_bar(number)
if number != 100:
    print(f"{number}% {loaded}")
    print("Still loading...")
else:
    print("100% Complete!")
    print(loaded)