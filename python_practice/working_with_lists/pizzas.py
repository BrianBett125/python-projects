# using a for loop to print three types of pizza
pizzas = ["cheese pizza", "peperoni pizza", "motzarella pizza"]
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the 
# following:
# • Add a new pizza to the original list
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My
# friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list
friend_pizzas = pizzas[:]
pizzas.append('cannabis')
friend_pizzas.append('pineaple')
print("\nmy favorite pizzas are: ")
print(pizzas)
print("\nmy friend's favorite pizzas are: ")
print(friend_pizzas)
for pizza in pizzas:
    print(f" I like {pizza.title()}!\n")
print(f" I really love pizza!")
