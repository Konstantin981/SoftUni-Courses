from math import ceil

series = input()
episode_time = int(input())
break_time = int(input())

lunch_time = 0.125*break_time
rest_time = 0.25*break_time

left=break_time-lunch_time-rest_time
if left>=episode_time:
    print(f"You have enough time to watch {series} and left with {ceil(left-episode_time):.0f} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(episode_time-left):.0f} more minutes.")