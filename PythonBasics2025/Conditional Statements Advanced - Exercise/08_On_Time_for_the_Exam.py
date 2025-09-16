exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_minutes = (exam_hour*60) + exam_minutes
arrival_minutes = (arrival_hour*60) + arrival_minutes

time_left = exam_minutes - arrival_minutes

time = ""

if time_left>30:
    time = "Early"
elif time_left<0:
    time="Late"
else:
    time = "On time"

hours = abs(time_left)//60
minutes = abs(time_left)%60

result = ""

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_left > 0:
    result += " before the start"

elif time_left < 0:
    result += " after the start"

print(time)
print(result)