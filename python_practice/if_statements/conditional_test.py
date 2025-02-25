# Write a series of conditional tests. Print a statement 
# describing each test and your prediction for the results of each test
# test 1
car = 'subaru'
print("is car == 'subaru', I predict True.")
print(car == 'subaru')

print("is car  == 'audi', I predict False.")
print(car == 'audi')

# test 2
food = 'chapati'
print("\nis food == 'chapati', I predict True")
print(food == 'chapati')

print("is food == 'dengu', I predict False")
print(food == 'dengu')

#test 3
cake = 'vanilla'
print("\nis cake  == 'vanilla', I predict True")
print(cake == 'vanilla')

print("is cake == 'red velvet', I predict False")
print(cake == 'red velvet')

# Tests for equality and inequality with strings
coffee = 'expreso'
if coffee == 'expreso':
    print(True)
else:
    print(False)

# Tests using the lower() method
print("\ntests using lower() method")
cars = 'Audi'
if cars.lower() == 'audi':
    print(True)

# Numerical tests involving equality and inequality, greater than and less 
# than, greater than or equal to, and less than or equal to
print("\ntest using keyword 'and' and 'or'")
num1 = 14
num2 = 21
if (num1 >= 12 and num2 >= 18):
    print(True)

if (num1 <  67 or num2 > 32):
    print(False)

if (num1 <= 9 or num2 >= 3):
    print(True)

# Test whether an item is in a list
print("\ntest whether item is in a list")
meals = ['meat', 'mushrooms', 'dessert']
meal = 'meat'
if 'meat' in meals:
    print(True)

# test whether an item is not in a list
print("\ntest whether an item is not in the list")
lost_people = ['otuki', 'nyambega', 'odoyo', 'michuki']
person = 'gatimu'
if person not in lost_people:
    print(f"{person.title()} is not the list of dissapeared students")
