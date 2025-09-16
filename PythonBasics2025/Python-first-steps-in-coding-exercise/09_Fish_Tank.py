lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())/100

total = lenght*width*height/1000
water = total - total*percent
print(water)
