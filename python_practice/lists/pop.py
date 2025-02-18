# removing items in a list using pop call
shoes = ['clarks', 'sharp shooters', 'boots', 'timberland', 'slippers']
print(shoes)

# adding a new variable 'rem_shoes'
remove_shoes = shoes.pop()
print(remove_shoes)
print(shoes)

# printing a message with the removed item
# we invoke a variable
favorite_shoe = shoes.pop(1)
message = f" the favorite shoe I owned was a: {favorite_shoe.upper()}!"
print(message)
