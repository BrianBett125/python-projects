# list_basics.ts

# 📘 Introduction to Python Lists

# Creating a list
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding elements
fruits.append("elderberry")
print("After append:", fruits)

# Inserting at a specific position
fruits.insert(2, "blueberry")
print("After insert:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

# Popping the last element
last = fruits.pop()
print("Popped:", last)
print("After pop:", fruits)

# Slicing the list
print("Slice [1:3]:", fruits[1:3])

# Looping through the list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)

# List comprehension
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)

