grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

sliced_grades = grades[2:8]
print("Sliced Grades (index 2 to 7):", sliced_grades)

above_85 = [grade for grade in grades if grade > 85]
print("Grades above 85:", above_85)

grades[3] = 95
print("After replacing index 3 with 95:", grades)

grades.extend([84, 93, 77])
print("After appending 3 new grades:", grades)

top_5 = sorted(grades, reverse=True)[:5]
print("Top 5 grades (descending):", top_5)
