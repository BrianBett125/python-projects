# Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following
# Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list
places = ['mombasa', 'nakuru', 'mogadishu', 'moyale', 'thika', 'mariakani', 'samburu']
print(places)
print("the first three items on a list are: ")
print(places[0:3])

# Print the message Three items from the middle of the list are:. Then use a 
# slice to print three items from the middle of the list.
print("\nthree items from the middle of the list are: ")
print(places[3:])

# Print the message The last three items in the list are:. Then use a slice to 
# print the last three items in the list.
print("\nthe last three items in the list are: ")
print(places[-3:])
