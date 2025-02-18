# removing element from a list using remove call
# N/B: The remove call removes items once and if the said item appears again in
# the list then you have to use a loop
# remove() method removes items if you don't know the position of an item
motocycles = ['kenegan', 'ktm', 'kawasaki', 'ninja', 'bmw']
print(motocycles)

# invoking the remove call
motocycles.remove('bmw')
print(motocycles)

# a message to print by invoking a variable
motocycles = ['kenegan', 'ktm', 'kawasaki', 'ninja', 'bmw']
expensive = 'bmw'
motocycles.remove(expensive)
print(f"\nA {expensive.upper()} is too expensive for me")
