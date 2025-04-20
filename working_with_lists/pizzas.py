# use a for loop to print names of each pizza
pizzas = ['cheese', 'pinneaple', 'peperoni']
my_friend_pizzas = pizzas[:]
pizzas.append('carrot')
my_friend_pizzas.append('lemonade')
# printig to check the list difference
print("my pizza\n")
print(pizzas)
print("\nmy_friend_pizzas")
print(my_friend_pizzas)
print("my favorite pizzas are:")
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")
print("I really love pizza")

for my_friend_pizza in my_friend_pizzas:
    print(f"\n\nmy friend likes {my_friend_pizza.title()} piza")
print("\nkevin really loves pizza")
