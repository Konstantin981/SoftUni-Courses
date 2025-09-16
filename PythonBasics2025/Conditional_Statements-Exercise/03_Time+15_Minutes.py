hours = int(input())
minutes = int(input())

minutes=minutes+15
if minutes>=60:
    minutes=minutes - 60
    hours = hours + 1
if hours == 24:
    hours = 0

if(minutes<10):
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")