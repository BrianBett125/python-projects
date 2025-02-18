# a list that invites three people to dinner and invites them
guest_list = ['aden', 'brian', 'mary']
print(f" \nwelcome {guest_list[0].title()} to my dinner party")
print(f" \nwelcome {guest_list[1].title()} to my dinner party")
print(f" \nwelcome {guest_list[-1].title()} to my dinner party")

# one of the guests can't make it. print the message
print(f"\n{guest_list[-1].title()} can't make it")

# Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting
del guest_list[-1]
guest_list.append('david')
print(guest_list)

# Print a second set of invitation messages, one for each person who
# is still in your list.
print(f" \nwelcome {guest_list[0].title()}!")
print(f" \nwelcome {guest_list[1].title()}!")
print(f" \nwelcome {guest_list[2].title()}!")

# Add a print() call to the end of your program,informing people that
# that you found a bigger table
print(f" \ndear {guest_list[0].title()}, {guest_list[1].title()} and {guest_list[2].title()},"
      " I have found a bigger table")

# Use insert() to add one new guest to the beginning of your list.
guest_list.insert(0, 'ivy')

# Use insert() to add one new guest to the middle of your list.
guest_list.insert(2, 'million')

#  Use append() to add one new guest to the end of your list.
guest_list.append('hassan')

print(guest_list)

# Print a new set of invitation messages, one for each person
# in your list.
print(f" welcome {guest_list[0].title()}")
print(f" welcome {guest_list[1].title()}")
print(f" welcome {guest_list[2].title()}")
print(f" welcome {guest_list[3].title()}")
print(f" welcome {guest_list[4].title()}")

# a new line that prints message that i can only invite 2 people
# for dinner
print(f" hello everyone, I can only"
        " invite two people for dinner")

# using pop() to remove people one at a time and sending them message
# saying sorry they are not invited
popped_name = guest_list.pop()
print(f" I am sorry {popped_name.title()}, I cannot invite you for dinner")

popped_name = guest_list.pop()
print(f" I am sorry {popped_name.title()}, I cannot invite you for dinner")

popped_name = guest_list.pop()
print(f" I am sorry {popped_name.title()}, I cannot invite you for dinner")

popped_name = guest_list.pop()
print(f" I am sorry {popped_name.title()}, I cannot invite you for dinner")

# Print a message to each of the two people still on your list,
# letting them know they’re still invited.
print(f" {guest_list[0]}, you are still invited")
print(f" {guest_list[1]}, you are still invited")

# Use del to remove the last two names from your list, so you
# have an empty list. Print your list to make sure you actually 
# have an empty list at the end of your program
del guest_list[0]
del guest_list[0]
print(guest_list)
