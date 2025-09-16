number  = int(input())
final = 0
bonus = 0

if number<=100:
    final = number + 5
    bonus = 5
elif 100<number<=1000:
    final = 1.2*number
    bonus = 0.2*number
elif 1000<number:
    final = number*1.1
    bonus = number*0.1

if number%2==0:
    final = final+1
    bonus += 1
elif number%10==5:
    final = final+2
    bonus += 2

print(bonus)
print (final)