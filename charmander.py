from pokemon import Pokemon

class Charmander(Pokemon):
  def __init__(self, name, level, type, is_knocked_out):
    super().__init__(name, level, type, is_knocked_out)
  
  def destroy(self, other):
    other.lose_health(other.health)
    print("{} totally destroyed {}!".format(self.name, other.name))
