# code to print cubes and make list of first ten cubes using for loop
# using a list comprehension
cubes = [value ** 3 for value in range(11)]
print(cubes)

# finding cubes
cubes = []
for value in range(11):
    cubes.append(value ** 3)
print(cubes)
