# contact_book.py

# This script creates a simple contact book using a Python dictionary.

def display_menu():
    print("\n==== Contact Book Menu ====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")

# Dictionary to store contact name as key and phone number as value
contacts = {}

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter contact name: ").strip().capitalize()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print(f"✅ Contact '{name}' added successfully.")

    elif choice == '2':
        if contacts:
            print("\n📒 Contact List:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    elif choice == '3':
        search_name = input("Enter the name to search: ").strip().capitalize()
        if search_name in contacts:
            print(f"📱 {search_name}'s number: {contacts[search_name]}")
        else:
            print(f"❌ No contact found for '{search_name}'.")

    elif choice == '4':
        print("👋 Exiting Contact Book. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter a number between 1 and 4.")

