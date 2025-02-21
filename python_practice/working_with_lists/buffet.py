# A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple
buffets = ('fish', 'chicken', 'steak', 'cake','dessert')
for buffet in buffets:
    print(buffet)

# Try to modify one of the items, and make sure that Python rejects the
# change.
buffets[0] = 'maharagwe'
print(buffets)

#  The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print 
# each of the items on the revised menu.
buffets = ('chapati', 'muthokoi', 'steak', 'cake', 'dessert')
print("\nmodified tuple list: ")
for buffet in buffets:
    print(buffet)
