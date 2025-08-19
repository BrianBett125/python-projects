from collections import defaultdict
import statistics

# Sample data: list of dictionaries
students = [
    {"name": "Alice", "grades": [78, 85, 90], "stream": "A"},
    {"name": "Bob", "grades": [60, 70, 72], "stream": "B"},
    {"name": "Charlie", "grades": [90, 92, 88], "stream": "A"},
    {"name": "Diana", "grades": [50, 55, 58], "stream": "C"},
    {"name": "Ethan", "grades": [95, 98, 100], "stream": "B"},
]

# 1. Calculate average grade for each student
for student in students:
    student["avg_grade"] = round(statistics.mean(student["grades"]), 2)

# 2. Sort students by average grade (descending)
students_sorted = sorted(students, key=lambda x: x["avg_grade"], reverse=True)

# 3. Group students by stream
stream_groups = defaultdict(list)
for student in students_sorted:
    stream_groups[student["stream"]].append(student)

# 4. Filter students who have avg grade above 80
top_students = [s for s in students_sorted if s["avg_grade"] > 80]

# 5. Display results
print("=== All Students (Sorted by Avg Grade) ===")
for s in students_sorted:
    print(f"{s['name']} ({s['stream']}) - Avg Grade: {s['avg_grade']}")

print("\n=== Students Grouped by Stream ===")
for stream, group in stream_groups.items():
    print(f"Stream {stream}: {[s['name'] for s in group]}")

print("\n=== Top Students (Avg > 80) ===")
for s in top_students:
    print(f"{s['name']} - {s['avg_grade']}")

