from random import choice

class Team:
    def __init__(self, name):
        self.name = name
        self.pokemons = list()

    def remove_pokemon(self, name):
        foundPoke = False
        for pokemon in self.pokemons:
            if pokemon.name == name:
                self.pokemons.remove(pokemon)
                foundPoke = True
        if not foundPoke:
            return 0
    
    def view_all_pokemons(self):
        """Print out all pokemons to the console."""
        for pokemon in self.pokemons:
            print(pokemon.name)
    
    def add_pokemon(self, pokemon):
        """Add pokemon object to self.pokemons."""
        self.pokemons.append(pokemon)
    
    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_pokes = list()
        living_opponents = list()

        for pokemon in self.pokemons:
            living_pokes.append(pokemon)

        for pokemon in other_team.pokemons:
            living_opponents.append(pokemon)

        while len(living_pokes) > 0 and len(living_opponents) > 0:
            rand_pokemon = choice(living_pokes)
            rand_opponent = choice(living_opponents)
            rand_pokemon.fight(rand_opponent)
            if rand_pokemon.is_alive() == True:
                living_opponents.remove(rand_opponent)
            elif rand_opponent.is_alive() == True:
                living_pokes.remove(rand_pokemon)
            else:
                living_opponents.remove(rand_opponent)
                living_pokes.remove(rand_pokemon)