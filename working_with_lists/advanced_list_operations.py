"""
advanced_list_operations.py

A deeply structured Python script demonstrating advanced and complex
operations involving lists, nested lists, comprehensions, list algorithms,
custom sorting, searching, filtering, classes using lists, and file interactions.

Author: Brian Bett (😉 if you use it)
"""

from functools import reduce
import random


# ------------------------------------------------------------
# 1. WORKING WITH NESTED LISTS
# ------------------------------------------------------------

def generate_matrix(rows, cols):
    """Generate a matrix of random integers."""
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]


def flatten_matrix(matrix):
    """Flatten a 2D matrix into a single list."""
    return [num for row in matrix for num in row]


def transpose_matrix(matrix):
    """Transpose a matrix (rows become columns)."""
    return list(map(list, zip(*matrix)))


# ------------------------------------------------------------
# 2. COMPLEX LIST COMPREHENSIONS & FILTERING
# ------------------------------------------------------------

def filter_even_numbers(numbers):
    """Return only even numbers using list comprehension."""
    return [n for n in numbers if n % 2 == 0]


def squares_of_large_values(numbers, threshold=50):
    """Return squares of numbers > threshold."""
    return [n * n for n in numbers if n > threshold]


def chunk_list(lst, size):
    """Split a list into chunks of a given size."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]


# ------------------------------------------------------------
# 3. LIST ALGORITHMS — SEARCHING & REDUCING
# ------------------------------------------------------------

def binary_search(sorted_list, target):
    """Binary search algorithm on a sorted list."""
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def sum_list(numbers):
    """Sum a list using reduce."""
    return reduce(lambda x, y: x + y, numbers)


# ------------------------------------------------------------
# 4. COMPLEX SORTING WITH CUSTOM KEYS
# ------------------------------------------------------------

def sort_students_by_grade(students):
    """
    students = [
        ("Brian", 85),
        ("Hassan", 92),
        ("Mitchell", 73)
    ]
    """
    return sorted(students, key=lambda x: x[1], reverse=True)


def sort_strings_by_vowels(words):
    """Sort strings by number of vowels."""
    vowels = "aeiou"
    return sorted(words, key=lambda word: sum(1 for c in word.lower() if c in vowels))


# ------------------------------------------------------------
# 5. USING LISTS INSIDE A CLASS
# ------------------------------------------------------------

class StudentList:
    """Manage a list of students with complex operations."""

    def __init__(self):
        self.students = []   # list of dicts: {"name":..., "grade":...}

    def add_student(self, name, grade):
        self.students.append({"name": name, "grade": grade})

    def top_students(self, count=3):
        sorted_students = sorted(self.students, key=lambda s: s["grade"], reverse=True)
        return sorted_students[:count]

    def average_grade(self):
        grades = [s["grade"] for s in self.students]
        return sum(grades) / len(grades) if grades else 0


# ------------------------------------------------------------
# 6. WORKING WITH FILES & LISTS
# ------------------------------------------------------------

def save_list_to_file(filename, lst):
    with open(filename, "w") as f:
        for item in lst:
            f.write(str(item) + "\n")


def load_list_from_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


# ------------------------------------------------------------
# 7. MAIN EXECUTION
# ------------------------------------------------------------

if __name__ == "__main__":

    print("\n--- MATRIX DEMONSTRATION ---")
    matrix = generate_matrix(4, 5)
    print("Original matrix:", matrix)
    print("Flattened:", flatten_matrix(matrix))
    print("Transposed:", transpose_matrix(matrix))

    print("\n--- LIST COMPREHENSIONS ---")
    nums = flatten_matrix(matrix)
    print("Even numbers:", filter_even_numbers(nums))
    print("Squares > 50:", squares_of_large_values(nums))

    print("\n--- CHUNKING ---")
    print(chunk_list(nums, 4))

    print("\n--- SEARCH & REDUCE ---")
    sorted_nums = sorted(nums)
    target = sorted_nums[len(sorted_nums) // 2]
    print("Binary search:", binary_search(sorted_nums, target))
    print("Sum:", sum_list(nums))

    print("\n--- CUSTOM SORTING ---")
    students = [("Brian", 88), ("Hassan", 95), ("Mitchell", 72), ("Faith", 90)]
    print("Sort by grade:", sort_students_by_grade(students))

    print("\n--- CLASS MANAGING LISTS ---")
    sl = StudentList()
    sl.add_student("Brian", 88)
    sl.add_student("Hassan", 95)
    sl.add_student("Mitchell", 72)
    print("Top students:", sl.top_students())
    print("Average grade:", sl.average_grade())

    print("\n--- FILE OPERATIONS ---")
    save_list_to_file("output.txt", nums)
    loaded = load_list_from_file("output.txt")
    print("Loaded list length:", len(loaded))


