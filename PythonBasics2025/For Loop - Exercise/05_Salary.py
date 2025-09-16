import math
FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

n = int(input())
salary = float(input())

for i in range(1, n+1):
    site_name = input()
    if site_name == "Facebook":
        salary -= FACEBOOK_FINE
    elif site_name == "Instagram":
        salary -= INSTAGRAM_FINE
    elif site_name == "Reddit":
        salary -= REDDIT_FINE

if salary<=0:
    print("You have lost your salary.")
else:
    print(f"{math.ceil(salary)}")