from pokemon import Pokemon
from trainer import Trainer
from team import Team

class Battle:
    def __init__(self):
        self.team_one: None
        self.team_two: None
    
    
    def create_pokemon(self):
        poke_name = input("Pokemon: ")
        poke_level = int(input("Level: "))
        poke_type = input("Type: ")
        pokemon = Pokemon(poke_name, poke_level, poke_type, False)
        return pokemon
    
    def create_trainer(self):
        trainer_name = input("Trainer: ")
        trainer_pokemon = input("Main Name: ")
        trainer_potions = int(input("Ammoount of Potions: "))
        trainer = Trainer(trainer_name, trainer_pokemon, trainer_potions)
        return trainer

    def create_team_one(self):
        team_name = input("Team Name: ")
        self.team_one = Team(team_name)

        self.create_trainer()
        pokemon = self.create_pokemon()
        self.team_one.add_pokemon(pokemon)
        
    
    def create_team_two(self):
        team_name = input("Team Name: ")
        self.team_two = Team(team_name)

        self.create_trainer()
        pokemon = self.create_pokemon()
        self.team_one.add_pokemon(pokemon)
    


        
    
    
    
        

    
    

# pikachu = Pokemon("Pikachu", 3, "Fire", False)
# bulbasaur = Pokemon("Bulbasaur", 3, "Grass", False)
# squirtle = Pokemon("Squirtle", 3, "Water", False)
# charmander = Charmander("Charmander", 3, "Fire", False)

# erika = Trainer('Erika', [pikachu], 2, pikachu)
# ramos = Trainer('Ramos', [bulbasaur, squirtle], 2, bulbasaur)

# print(pikachu)
# print(bulbasaur)

# pikachu.lose_health(1)
# pikachu.gain_health(1)
# pikachu.gain_exp(3)

if __name__ == "__main__":
    game_is_running = True
    battle = Battle()

    while True:
        print("Welcome")
        battle.create_pokemon()
        break