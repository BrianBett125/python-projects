# Simple Shopping Cart using Python Dictionaries

# Product catalog with prices
products = {
    'apple': 30,
    'banana': 20,
    'mango': 50,
    'orange': 25
}

# Empty cart
cart = {}

print("Welcome to the Fruit Store 🍎🍌🥭🍊")
print("Available products:")
for item, price in products.items():
    print(f"{item.title()} - Ksh {price}")

# Adding items to the cart
while True:
    choice = input("\nEnter the product name to add to cart (or 'done' to finish): ").lower()
    if choice == 'done':
        break
    if choice in products:
        quantity = int(input(f"How many {choice}s would you like to buy? "))
        # Add or update the quantity in the cart
        cart[choice] = cart.get(choice, 0) + quantity
        print(f"✅ Added {quantity} {choice}(s) to your cart.")
    else:
        print("❌ Product not found. Please try again.")

# Display the cart summary
print("\n🛍️ Your Shopping Cart:")
total = 0
for item, quantity in cart.items():
    price = products[item] * quantity
    total += price
    print(f"{item.title()} x{quantity} = Ksh {price}")

# Display total cost
print(f"\n💰 Total Amount: Ksh {total}")

# Option to remove an item
remove_item = input("\nDo you want to remove an item? (yes/no): ").lower()
if remove_item == 'yes':
    item_to_remove = input("Enter the product name to remove: ").lower()
    if item_to_remove in cart:
        del cart[item_to_remove]
        print(f"🗑️ {item_to_remove.title()} removed from your cart.")
    else:
        print("❌ That item is not in your cart.")

# Final cart
print("\n🧾 Final Cart Summary:")
for item, quantity in cart.items():
    print(f"{item.title()} x{quantity}")
print("Thank you for shopping with us! 🛒")

