people_in_queue = int(input())
lift = list(map(int, input().split()))
for i in range(len(lift)):
    free_spots = 4 - lift[i]
    if people_in_queue >= free_spots:
        lift[i] += free_spots
        people_in_queue -= free_spots
    else:
        lift[i] += people_in_queue
        people_in_queue = 0
        break
if people_in_queue == 0 and any(wagon < 4 for wagon in lift):
    print("The lift has empty spots!")
    print(" ".join(map(str, lift)))
elif people_in_queue > 0 and all(wagon == 4 for wagon in lift):
    print(f"There isn't enough space! {people_in_queue} people in a queue!")
    print(" ".join(map(str, lift)))
else:
    print(" ".join(map(str, lift)))
