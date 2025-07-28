employees = [
    ("Alice", 50000, "Engineering"),
    ("Bob", 60000, "Marketing"),
    ("Carol", 55000, "Engineering"),
    ("David", 45000, "Sales")
]

# 1. Sort by Salary (Ascending)
sorted_by_salary_asc = sorted(employees, key=lambda e: e[1])
print("Sorted by Salary (Ascending):")
print(sorted_by_salary_asc)

# Sort by Salary (Descending)
sorted_by_salary_desc = sorted(employees, key=lambda e: e[1], reverse=True)
print("\nSorted by Salary (Descending):")
print(sorted_by_salary_desc)

# 2. Sort by Department, then by Salary
sorted_by_dept_then_salary = sorted(employees, key=lambda e: (e[2], e[1]))
print("\nSorted by Department, then by Salary:")
print(sorted_by_dept_then_salary)

# 3. Create a Reversed List (without modifying original)
reversed_list = list(reversed(employees))
print("\nReversed List (without modifying original):")
print(reversed_list)

# 4. Sort by Name Length
sorted_by_name_length = sorted(employees, key=lambda e: len(e[0]))
print("\nSorted by Name Length:")
print(sorted_by_name_length)

# 5. .sort() vs sorted() demonstration
employees_copy = employees.copy()
employees_copy.sort(key=lambda e: e[1])
print("\nOriginal list sorted by salary using .sort():")
print(employees_copy)

# Using sorted() to create a new list sorted by department
sorted_by_dept = sorted(employees, key=lambda e: e[2])
print("\nNew list sorted by department using sorted():")
print(sorted_by_dept)
