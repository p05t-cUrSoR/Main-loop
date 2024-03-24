import random
import pickle

# Define NPC class
class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

# Define Quest class
class Quest:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

# Define Location class
class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.interactions = []

# Define Player class
class Player:
    def __init__(self, name, health=100, inventory=None):
        self.name = name
        self.health = health
        self.inventory = inventory if inventory is not None else []
        self.completed_quests = []
        self.current_location = None

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def remove_item_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item not found in inventory.")

# Initialize NPCs
def initialize_npcs():
    npcs = {
        "Captain Picard": NPC("Captain Picard", ["Welcome aboard the USS Enterprise.", "Make sure to report any anomalies."]),
        "Counselor Troi": NPC("Counselor Troi", ["Hello, how can I assist you?", "I seem to have lost something quite personal..."]),
        # Add more NPCs as needed
    }
    return npcs

# Initialize quests
def initialize_quests():
    quests = {
        "Investigate Anomaly": Quest("Investigate Anomaly", "Investigate the anomaly in the Beta Quadrant."),
        "Find Troi's Missing Item": Quest("Find Troi's Missing Item", "Help Counselor Troi find her missing item."),
        # Add more quests as needed
    }
    return quests

# Initialize locations
def initialize_locations():
    locations = {
        "Bridge": Location("Bridge", "The nerve center of the USS Enterprise."),
        "Counselor's Office": Location("Counselor's Office", "Where Counselor Troi offers guidance to the crew."),
        # Add more locations as needed
    }
    return locations

# Function to process player's interaction choice
def process_interaction(player, choice):
    location = player.current_location
    interaction = location.interactions[choice]
    
    if interaction == "Talk to Captain Picard":
        npc = npcs["Captain Picard"]
        for line in npc.dialogue:
            print(line)
    elif interaction == "Talk to Counselor Troi":
        npc = npcs["Counselor Troi"]
        for line in npc.dialogue:
            print(line)
    # Add more interactions as needed

# Function to check quest completion
def check_quest_completion(player):
    for quest_name, quest in quests.items():
        if quest_name not in player.completed_quests and quest.completed:
            player.completed_quests.append(quest_name)
            print(f"Congratulations! You have completed the quest: {quest_name}")

# Function to save game progress
def save_game(player):
    with open("save_game.pkl", "wb") as f:
        pickle.dump(player, f)
    print("Game progress saved.")

# Function to load game progress
def load_game():
    try:
        with open("save_game.pkl", "rb") as f:
            player = pickle.load(f)
        print("Game progress loaded.")
        return player
    except FileNotFoundError:
        print("No saved game found.")
        return None

# Main function
def main():
    print("Welcome to Star Trek: The Next Generation RPG!")
    player_name = input("Enter your name: ")
    
    # Attempt to load saved game progress
    player = load_game()
    
    if player is None:
        # If no saved game found, create a new player
        player = Player(player_name)

        # Initialize game data
        global npcs, quests, locations
        npcs = initialize_npcs()
        quests = initialize_quests()
        locations = initialize_locations()

        # Set player's initial location
        player.current_location = locations["Bridge"]

    # Main game loop
    while True:
        print(f"You are currently at {player.current_location.name}: {player.current_location.description}")
        print("Available interactions:")
        for idx, interaction in enumerate(player.current_location.interactions):
            print(f"{idx + 1}. {interaction}")
        
        choice = input("Choose an interaction: ")
        if choice.isdigit():
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(player.current_location.interactions):
                process_interaction(player, choice_index)
                check_quest_completion(player)
                save_game(player)  # Save game progress after each interaction
            else:
                print("Invalid choice. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a number.")

# Call the main function
if __name__ == "__main__":
    main()
