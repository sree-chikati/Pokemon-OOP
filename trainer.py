class Trainer:
  def __init__(self, name, pokemon, potions):
    self.name = name
    self.pokemon = pokemon
    self.potions = potions
  
  def trainer_info(self):
    #return "Trainer info. {name}, has pokemons: {pokemons}, has {potions} potions, current pokemon is {current_pokemon}.".format(name = self.name, pokemons = self.pokemons, potions = self.potions, current_pokemon = self.current_pokemon)
    return f"\nTrainer info:\n name: {self.name}\n Pokemons: {self.pokemon}\n Type: {self.potions}\n"
  
  def use_potion(self):
    if self.potions > 0:
      if self.pokemon.health < self.pokemon.max_health:
        self.pokemon.gain_health(1)
        self.potions -= 1
        print("{} has {} potions left.\n".format(self.name, self.potions))
      else:
        print("{} failed to use a potion on {}. Your pokemon has maximum health.\n".format(self.name, self.pokemon.name))
    else:
      print("{}, you have no potions!\n".format(self.name))
  