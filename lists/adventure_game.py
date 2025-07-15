# Text-based adventure game

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Dictionary of direction: room
        self.items = []  # List of items in the room

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item
        return None

    def __str__(self):
        result = f"\n{self.name}\n{'-' * len(self.name)}\n{self.description}\n"
        if self.items:
            result += "Items in room:\n"
            for item in self.items:
                result += f"- {item}\n"
        result += "Exits: " + ", ".join(self.exits.keys()) + "\n"
        return result

class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            return True
        return False

    def take_item(self, item_name):
        item = self.current_room.remove_item(item_name)
        if item:
            self.inventory.append(item)
            return True
        return False

    def drop_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                self.current_room.add_item(item)
                return True
        return False

    def show_inventory(self):
        if not self.inventory:
            return "Your inventory is empty."
        return "Inventory:\n" + "\n".join(str(item) for item in self.inventory)

class Game:
    def __init__(self):
        self.rooms = {}
        self.setup_rooms()
        self.player = Player(self.rooms["hall"])
        self.is_running = True

    def setup_rooms(self):
        # Create rooms
        hall = Room("Hall", "A grand hall with high ceilings and dusty chandeliers.")
        kitchen = Room("Kitchen", "An old kitchen with rusty utensils and a creaky floor.")
        library = Room("Library", "A dusty library filled with ancient books.")
        garden = Room("Garden", "An overgrown garden with tangled vines and colorful flowers.")

        # Create items
        key = Item("Key", "A small rusty key that looks important.")
        book = Item("Book", "An ancient tome with strange symbols.")
        flower = Item("Flower", "A vibrant red flower with a sweet scent.")

        # Add items to rooms
        kitchen.add_item(key)
        library.add_item(book)
        garden.add_item(flower)

        # Set up exits
        hall.add_exit("north", kitchen)
        hall.add_exit("east", library)
        kitchen.add_exit("south", hall)
        kitchen.add_exit("east", garden)
        library.add_exit("west", hall)
        garden.add_exit("west", kitchen)

        # Store rooms
        self.rooms["hall"] = hall
        self.rooms["kitchen"] = kitchen
        self.rooms["library"] = library
        self.rooms["garden"] = garden

    def display_help(self):
        return """Commands:
        go [direction] - Move to another room (north, south, east, west)
        take [item] - Pick up an item
        drop [item] - Drop an item
        inventory - Show your inventory
        look - Look around the current room
        help - Show this help message
        quit - Exit the game"""

    def process_command(self, command):
        parts = command.lower().strip().split()
        if not parts:
            return "Please enter a command."

        action = parts[0]
        
        if action == "quit":
            self.is_running = False
            return "Thanks for playing!"
        
        if action == "help":
            return self.display_help()
        
        if action == "look":
            return str(self.player.current_room)
        
        if action == "inventory":
            return self.player.show_inventory()
        
        if action == "go" and len(parts) > 1:
            direction = parts[1]
            if self.player.move(direction):
                return str(self.player.current_room)
            return f"Cannot go {direction} from here."
        
        if action == "take" and len(parts) > 1:
            item_name = " ".join(parts[1:])
            if self.player.take_item(item_name):
                return f"Took {item_name}."
            return f"No {item_name} found in the room."
        
        if action == "drop" and len(parts) > 1:
            item_name = " ".join(parts[1:])
            if self.player.drop_item(item_name):
                return Kardashian: return f"Dropped {item_name}."
            return f"You don't have a {item_name}."
        
        return "Invalid command. Type 'help' for commands."

    def play(self):
        print("Welcome to the Adventure Game!")
        print(self.display_help())
        print(str(self.player.current_room))

        while self.is_running:
            command = input("> ")
            print(self.process_command(command))

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
