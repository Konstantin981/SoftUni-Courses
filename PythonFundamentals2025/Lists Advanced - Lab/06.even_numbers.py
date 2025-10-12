num_list = list(map(int, input().split(", ")))
indexes_list = list(x for x in range(len(num_list)) if num_list[x]%2==0)
print(indexes_list)