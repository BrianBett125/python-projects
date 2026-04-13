# Creating a dictionary
student = {
    'name': 'John Doe',
    'age': 20,
    'grade': 'A',
    'subjects': ['Math', 'Science', 'History']
}

# Accessing values
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")

# Updating values
student['age'] = 21
student['grade'] = 'A+'
print("\nUpdated Information:")
print(f"Age: {student['age']}")
print(f"Grade: {student['grade']}")

# Adding new key-value pair
student['address'] = '1234 Elm Street'
print("\nAfter Adding Address:")
print(f"Address: {student['address']}")

# Checking if a key exists
if 'subjects' in student:
    print("\nSubjects: ", student['subjects'])
else:
    print("Subjects key not found.")

# Iterating over dictionary
print("\nStudent Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Deleting a key-value pair
del student['address']
print("\nAfter Deleting Address:")
print(student)

# Dictionary methods
keys = student.keys()
values = student.values()
print("\nKeys in the dictionary:", keys)
print("Values in the dictionary:", values)

