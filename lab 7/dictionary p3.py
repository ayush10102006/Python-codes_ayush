from collections import defaultdict
employees = [
    (101, 1, 50000),
    (101, 2, 60000),
    (101, 3, 55000),
]
dept_salaries = defaultdict(list)
for dept, roll, salary in employees:
    dept_salaries[dept].append(salary)
for dept, salaries in dept_salaries.items():
    print(f"Department {dept}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")
