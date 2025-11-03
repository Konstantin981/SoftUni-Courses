company_users = {}
command = input()
while command != "End":
    command = command.split(" -> ")
    company = command[0]
    user_id = command[1]
    if company not in company_users:
        company_users[company] = []
        company_users[company].append(user_id)
    else:
        if user_id not in company_users[company]:
            company_users[company].append(user_id)
    command = input()

for key, value in company_users.items():
    print(key)
    for user in value:
        print(f"-- {user}")