# a tuple: an immutable list(cannot change) 
dimensions = (989, 400)
print(dimensions[0])
print(dimensions[1])
print("\noriginal dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (167, 987)
print("\nmodified dimensions")
for dimension in dimensions:
    print(dimensions)
