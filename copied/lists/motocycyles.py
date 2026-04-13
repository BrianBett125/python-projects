# modifying items in a list
motocycles = ['ducati', 'yamaha', 'kawasaki']
print(motocycles)

motocycles[0] = 'ninja h2r'
print(motocycles)

# adding items to the list
print("\nadding items using append()")
motocycles.append('bmw')
motocycles.append('electro')
print(motocycles)

print("\nadding items to the list using insert()")
motocycles.insert(2, 'ghost')
print(motocycles)

# removing items from the list
print("\nremoving items from a list using del statement")
del motocycles[-1]
print(motocycles)

print("\nremoving items using pop() method")
popped_motocycle = motocycles.pop()
# pop removes last item in the list which can be re-used
print(motocycles)

print("\nprinting a message with the popped item")
last_popped = motocycles.pop()
print(f"my last owned motocycle was {last_popped.title()}.")

# removing items using pop with known location in a list
print("\nremoving the second item using pop")
motocycles.pop(1)
print(motocycles)

# removing items by value(here we dont use name)
print("\nremoving an item by value using remove()")
motocycles.remove('ninja h2r')
print(motocycles)
