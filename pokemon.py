import random
from move import Move
from potion import Potion
from item import Item

class Pokemon: 
     def __init__(self, name, starting_health=100):
         self.moves = list()
         self.potions = list()
         self.name = name
         self.starting_health = starting_health
         self.current_health = starting_health
         self.alive_status = True
         self.deaths = 0
         self.kills = 0
    
     def add_move(self, move):
        self.moves.append(move)
    
     def add_item(self, item):
        self.moves.append(item)

     def add_potion(self, potion):
         self.potions.append(potion)

     def attack(self):
         total_damage = 0
         for ability in self.moves:
             damage = ability.attack()
             total_damage += damage
         return total_damage

     def heal(self):
         total_heal = 0
         for move in self.moves:
             total_heal += move.heal()
         return total_heal
     
     def take_damage(self, damage):
         self.current_health -= damage + self.heal()
         if self.current_health < 0:
             self.current_health = 0

     def is_alive(self):  
         if self.current_health <= 0:
             return False
         else:
             return True

     def fight(self, opponent):  
         if len(self.starting_health) == 0 and len(opponent.starting_health) == 0:
             print("Draw")
             return

         while self.is_alive() and opponent.is_alive():
             self.take_damage(opponent.attack())
             opponent.take_damage(self.attack())

             if self.is_alive() == False:
                 print(f"{opponent.name} wins!")

             elif opponent.is_alive() == False:
                 print(f"{self.name} wins!")