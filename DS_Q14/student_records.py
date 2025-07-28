students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 19),
    (103, "Carol", 78, 21),
    (104, "David", 88, 20)
]

# 1. Find the Student with the Highest Grade
highest = max(students, key=lambda s: s[2])
print("Student with the highest grade:", highest)

# 2. Create a Name-Grade List
name_grade_list = [(s[1], s[2]) for s in students]
print("Name-Grade List:", name_grade_list)

# 3. Demonstrate Tuple Immutability
try:
    students[0][2] = 95
except TypeError as e:
    print("Tuple Immutability Error:", e)
