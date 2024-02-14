employee_salaries = {}

while True:
    name = input("Enter employee name (or 'no' to exit): ")
    if name.lower() == 'no':
        break
    salary = float(input("Enter employee salary: "))
    employee_salaries[name] = salary

print("\nEmployee Salaries:")
for name, salary in employee_salaries.items():
    print(f"{name}: {salary}")