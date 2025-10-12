N = int(input())
more_chairs = 0
enough = True
for i in range(N):
    chairs_and_people = input().split()
    if len(chairs_and_people[0]) < int(chairs_and_people[1]):
        needed_chairs = int(chairs_and_people[1]) - len(chairs_and_people[0])
        print(f"{needed_chairs} more chairs needed in room {i+1}")
        enough = False
    else:
        more_chairs += len(chairs_and_people[0]) - int(chairs_and_people[1])

if enough:
    print(f"Game On, {more_chairs} free chairs left")