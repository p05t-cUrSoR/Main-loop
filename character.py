class Character:
    def __init__(self, name, health=100, inventory=None):
        self.name = name
        self.health = health
        self.inventory = inventory or []
        self.completed_quests = []
        self.current_location = None

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def remove_item_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item not found in inventory.")

def create_character():
    name = input("Enter your name: ")
    return Character(name)
