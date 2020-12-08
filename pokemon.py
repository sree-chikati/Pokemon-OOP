class Pokemon:
  def __init__(self, name, level, type, is_knocked_out):
    self.name = name
    self.level = level
    self.type = type
    self.is_knocked_out = is_knocked_out
    self.exp = 0
    self.max_health = level
    self.health = self.max_health
  
  def pokemon_info(self):
    #return "Pokemon info. {}, current level: {}, type: {}, maximun health: {}, current health: {}.\n".format(self.name, self.level, self.type, self.max_health, self.health)
    return f"\nPokemon info:\n name: {self.name}\n current level: {self.level}\n type: {self.type}\n current health:{self.health}\n max health:{self.max_health}\n "
  
  def lose_health(self, dmg):
    self.health -= dmg
    if self.health <= 0:
      self.health = 0
      self.knock_out()
  
  def gain_health(self, heal):
    self.health += heal
    print("{} gained {} health".format(self.name, heal))
    print("{}'s health: {}".format(self.name, self.health))
  
  def knock_out(self):
    if self.is_knocked_out:
      print("{name} is already knocked out.".format(name = self.name))
    else:
      self.is_knocked_out = True
      print("{name} is knocked out!".format(name = self.name))
  
  def revive(self):
    if self.is_knocked_out:
      self.is_knocked_out = False
      self.health = 1
      print("{name} has been revived with {health} health!".format(name = self.name, health = self.health))
    else:
      print("{name} is not knocked out.".format(name = self.name))
  
  def attack(self, other, dmg):
    if self.is_knocked_out == True:
      print("You can not attack. {pokemon} is knocked out!".format(pokemon = self.name))
      return
    if self.type == 'Water':
      if other.type == 'Fire':
        dmg *= 2
      elif other.type == 'Grass':
        dmg /= 2
    elif self.type == 'Fire':
      if other.type == 'Grass':
        dmg *= 2
      elif other.type == 'Water':
        dmg /= 2
    elif self.type == 'Grass':
      if other.type == 'Water':
        dmg *= 2
      elif other.type == 'Fire':
        dmg /= 2
    other.lose_health(dmg)
    print("{} attacked {}".format(self.name, other.name))
    print("{} dealt {} damage to {}. His health is {}.".format(self.name, dmg, other.name, other.health))
    self.gain_exp(1)
  
  def gain_exp(self, exp):
    self.exp += exp
    print("{} gained {} xp.\n".format(self.name, exp))
    if self.exp >= 3:
      self.level_up()
  
  def level_up(self):
    self.exp = 0
    self.level += 1
    self.max_health += 1
    self.health = self.max_health
    print("{} leveled up to level {}! Max health now is {}. Health fully regenerated.\n".format(self.name, self.level, self.max_health))