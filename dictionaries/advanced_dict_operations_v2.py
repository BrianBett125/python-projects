from collections import defaultdict

# Creating a dictionary of students with their grades
students_grades = {
    'John': 85,
    'Jane': 90,
    'Tom': 78,
    'Lucy': 92,
    'Mike': 88
}

# Sorting the dictionary by values (grades)
sorted_students = dict(sorted(students_grades.items(), key=lambda item: item[1], reverse=True))
print("Sorted Students by Grades (Descending):")
print(sorted_students)

# Using defaultdict for handling missing keys
student_courses = defaultdict(list)

# Adding courses for students (without worrying about key errors)
student_courses['John'].append('Math')
student_courses['Jane'].append('Science')
student_courses['Tom'].append('History')

print("\nStudent Courses (Using defaultdict):")
print(student_courses)

# Nested dictionary example - storing student info
students_info = {
    'John': {'age': 20, 'grade': 'B', 'courses': ['Math', 'Science']},
    'Jane': {'age': 22, 'grade': 'A', 'courses': ['Math', 'History']},
    'Tom': {'age': 19, 'grade': 'C', 'courses': ['History', 'Art']},
}

# Accessing nested dictionary values
print("\nJohn's Info:")
print(f"Age: {students_info['John']['age']}")
print(f"Grade: {students_info['John']['grade']}")
print(f"Courses: {students_info['John']['courses']}")

# Updating nested dictionary value
students_info['Tom']['grade'] = 'B'
print("\nUpdated Tom's Grade:")
print(students_info['Tom']['grade'])

# Nested dictionary with a list of dictionaries (more complex data structure)
students_list_info = [
    {'name': 'John', 'age': 20, 'grade': 'B'},
    {'name': 'Jane', 'age': 22, 'grade': 'A'},
    {'name': 'Tom', 'age': 19, 'grade': 'C'},
]

# Filtering students with grade 'A'
top_students_list = [student for student in students_list_info if student['grade'] == 'A']
print("\nTop Students with Grade 'A':")
print(top_students_list)

# Using dict comprehension to create a new dictionary based on condition
students_above_20 = {student['name']: student['age'] for student in students_list_info if student['age'] > 20}
print("\nStudents Above Age 20:")
print(students_above_20)

