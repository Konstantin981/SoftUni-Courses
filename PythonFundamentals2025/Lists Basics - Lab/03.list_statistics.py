n = int(input())
positive_list = []
negative_list = []
count_positive = 0
sum_negative = 0
for i in range(n):
    num = int(input())
    if num >= 0:
        positive_list.append(num)
        count_positive += 1
    else:
        negative_list.append(num)
        sum_negative += num

print(positive_list)
print(negative_list)
print(f"Count of positives: {count_positive}")
print(f"Sum of negatives: {sum_negative}")