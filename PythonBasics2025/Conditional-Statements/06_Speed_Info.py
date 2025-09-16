
number = float(input())

if number <= 10:
    print("slow")
elif 10<number<=50:
    print("average")
elif 50<number<=150:
    print("fast")
elif 150<number<=1000:
    print("ultra fast")
else:
    print ("extremely fast")