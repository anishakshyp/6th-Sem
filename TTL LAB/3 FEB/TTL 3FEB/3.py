n = int(input("Enter the Number of employees: "))
employee_dict = {}

for _ in range(n):
    name = input("Enter employee name: ")
    department = input("Enter employee department: ")
    employee_dict[name] = department

print("Employee Dictionary:", employee_dict)
