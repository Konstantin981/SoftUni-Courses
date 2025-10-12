def happiness_check(employees_lst, improvement_factor):
    improved_lst = [x*improvement_factor for x in employees_lst]
    sum_happiness = sum(improved_lst)
    average_happiness = sum_happiness/len(employees_lst)
    happy_employees = sum(num>=average_happiness for num in improved_lst    )
    message = "happy" if happy_employees >= len(employees_lst)/2 else "not happy"
    return f"Score: {happy_employees}/{len(employees_lst)}. Employees are {message}!"

employees_lst = list(map(int, input().split()))
improvement_factor = int(input())
output = happiness_check(employees_lst, improvement_factor)
print(output)