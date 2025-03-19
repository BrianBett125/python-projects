# using strip() on a variable used to represent a person's name and print
name = " ada lovelace "
print("removing the whitespace on the left")
print(f"\t{name.lstrip()}")
print("\nremoving the whitespace in the right")
print(f"\t{name.rstrip()}")
print("\nremoving the whitespace on both sides")
print(f"\t{name.strip()}")
