company_users = {}
while True:
    line = input()
    if line == "End":
        break
    company_name, employee_id = line.split(" -> ")
    if company_name not in company_users.keys():
        company_users[company_name] = []

    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)

for company, employee in company_users.items():
    print(f"{company}")
    for current_employee in employee:
        print(f"-- {current_employee}")
