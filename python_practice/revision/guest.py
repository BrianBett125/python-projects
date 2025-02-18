## Inviting guests to dinner
guests = ['david', 'aden', 'brian', 'million']
print(f" Welcome {guests[0].title()} to dinner")
print(f" Welcome {guests[1].title()} to dinner")
print(f" Welcome {guests[2].title()} to dinner")
print(f" Welcome {guests[-1].title()} to dinner")

## changing guest list by using remove
remove_guest = 'million'
guests.remove(remove_guest)
print(f" {remove_guest.title()} cannot make it to dinner")

## changing guest list by using pop
popped_guest = guests.pop()
print(f" {popped_guest.title()} cannot make it to dinner")

## inviting a new guest
guests.append('mary')
print(f" welcome {guests[0].title()}")
print(f" Welcome {guests[1].title()}")
print(f" welcome {guests[2].title()}")

## more guests
print(f" Hello, {guests[0].title()}, {guests[1].title()}, {guests[2].title()}"
        " we've found a bigger table")
guests.insert(0, 'moya')
guests.insert(2, 'muchacho')
guests.append('kipyegon')
print(guests)
print(f" welcome {guests[0].title()}, {guests[1].title()}, {guests[2].title()}, {guests[3].title()}, {guests[4].title()} and {guests[5].title()} to this party")

## shrinking guest list
print(f"\nI can only invite two people to dinner")
guests.pop()
print(f" sorry {guests[-1].title()}, I cannot invite you to dinner")
guests.pop()
print(f" sorry {guests[-1].title()}, I cannot invite you to dinner")
guests.pop()
print(f" sorry {guests[-1].title()}, I cannot invite you to dinner")
guests.pop()
print(f" sorry {guests[-1].title()}, I cannot invite you to dinner")
print(guests)
print(f" welcome {guests[0].title()} to the party")
print(f" welcome {guests[1].title()} to the party")

## deleting the entire list using del
del guests[1]
del guests[0]
print(guests)
