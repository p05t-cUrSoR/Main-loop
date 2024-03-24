import pickle
from character import Character, create_character
from npc import initialize_npcs
from quest import initialize_quests
from location import initialize_locations

class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

class Quest:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.completed = False

class Location:
    def __init__(self, name, desc, inter=None):
        self.name = name
        self.desc = desc
        self.inter = inter or []

def process_interaction(player, choice):
    location = player.current_location
    npc = location.inter[choice].npc if "Talk" in location.inter[choice] else None
    if npc:
        for line in npc.dialogue:
            print(line)

def check_quest_completion(player):
    for quest_name, quest in player.quests.items():
        if quest.completed and quest_name not in player.completed_quests:
            player.completed_quests.append(quest_name)
            print(f"Congratulations! You've completed the quest: {quest_name}")

def save_game(player):
    with open("save_game.pkl", "wb") as f:
        pickle.dump(player, f)
    print("Game progress saved.")

def load_game():
    try:
        with open("save_game.pkl", "rb") as f:
            player = pickle.load(f)
        print("Game progress loaded.")
        return player
    except FileNotFoundError:
        print("No saved game found.")
        return None

def main():
    print("Welcome to Star Trek: The Next Generation RPG!")
    player_name = input("Enter your name: ")
    player = load_game() or create_character(name=player_name)
    
    if player.current_location is None:
        player.npcs = initialize_npcs()
        player.quests = initialize_quests()
        player.locations = initialize_locations()
        player.current_location = player.locations["Bridge"]
    
    while True:
        print(f"You are currently at {player.current_location.name}: {player.current_location.desc}")
        print("Available interactions:")
        for idx, interaction in enumerate(player.current_location.inter):
            print(f"{idx + 1}. {interaction}")
        
        choice = input("Choose an interaction: ")
        if choice.isdigit():
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(player.current_location.inter):
                process_interaction(player, choice_index)
                check_quest_completion(player)
                save_game(player)
            else:
                print("Invalid choice. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
