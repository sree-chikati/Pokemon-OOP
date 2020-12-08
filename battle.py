from move import Move
from item import Item
from potion import Potion
from pokemon import Pokemon
from team import Team
from trainer import Trainer

class Battle:
    def __init__(self):
        self.team_one: None
        self.team_two: None
    
    def create_move(self):
        move_add = input("[1] Fire moves\n[2] Water moves[3] Grass moves\n\nYour choice:   ")
        if move_add == "1":
            name = 'Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'
        elif move_add == "2":
            name = 'Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'
        elif move_add == "3":
            name = 'Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'
        max_damage = input(
            "What is the max damage of the move?  ")

        return Move(name, max_damage)
    
    def create_item(self):
        name = input("What is the item's name?  ")
        max_damage = input(
            "What is the max damage of the item?  ")
    
        return Item(name, max_damage)
    
    def create_potion(self):
        name = input("What is the potion's name?  ")
        max_defense = input(
            "What is the max defense of the potion?  ")
    
        return Potion(name, max_defense)
    
    def create_pokemon(self):
        poke_name = input("Enter Pokemon's name: ")
        pokemon = Pokemon(poke_name)
        add_choice = None
        while add_choice != "3":
           add_choice = input("[1] Add move\n[2] Add item\n[3] Done adding items\n\nYour choice: ")
           if add_choice == "1":
               move = self.create_move()
               pokemon.add_move(move)
           elif add_choice == "2":
               item = self.create_item()
               pokemon.add_item(item)
        return pokemon
    
    def create_trainer(self):
        trainer_name = input("\nTrainer: ")
        trainer_pokemon = input("Main Pokemon\n Options are Kanto starters (Charmander, Squirtle, Bulbasaur): ")
        num_potions = int(input("Ammoount of Potions: "))
        trainer = Trainer(trainer_name, trainer_pokemon, num_potions)
        return trainer


    def build_team_one(self):
        team_name = input("What is the name of the first team? ")
        self.team_two = Team(team_name, 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
        self.create_trainer()

        for i in range(1):
            pokemon = self.create_pokemon()
            self.team_one.add_pokemon(pokemon)

    def build_team_two(self):
        team_name = input("What is the name of the second team? ")
        self.team_two = Team(team_name, 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':8, 'DEFENSE':12})
        self.create_trainer()

        for i in range(1):
            pokemon = self.create_pokemon()
            self.team_two.add_pokemon(pokemon)
    
    def team_battle(self):
        self.team_one.fight(self.team_two)
    
    


if __name__ == "__main__":
    game_is_running = True
    battle = Battle()
    
    print("Welcome to the Pokemon Gym Battle! Please Register your team first so we can get started!")
    battle.build_team_one()
    battle.build_team_two()

    while game_is_running:

        battle.team_battle()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            print("Thank you for joining us in battle! That was an exciting match!")
            game_is_running = False

        else:
            battle.team_battle()
