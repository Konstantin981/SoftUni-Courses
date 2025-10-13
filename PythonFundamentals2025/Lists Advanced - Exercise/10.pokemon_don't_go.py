distances_as_strings = input().split()
distances = [int(x) for x in distances_as_strings]
sum = 0
while not (distances == []):
    index = int(input())
    if index<0:
        current_value = distances[0]
        sum+=current_value
        distances.pop(0)
        distances.insert(0,distances[len(distances)-1])
        for i in range(len(distances)):
            if distances[i]<=current_value:
                distances[i]+= current_value
            else:
                distances[i] -= current_value
    elif index > len(distances)-1:
        current_value = distances[len(distances)-1]
        sum+=current_value
        distances.pop(len(distances)-1)
        distances.insert(len(distances), distances[0])
        for i in range(len(distances)):
            if distances[i] <= current_value:
                distances[i] += current_value
            else:
                distances[i] -= current_value
    else:
        current_value = distances[index]
        sum+=current_value
        distances.pop(index)
        for i in range(len(distances)):
            if distances[i] <= current_value:
                distances[i] += current_value
            else:
                distances[i] -= current_value
print(sum)