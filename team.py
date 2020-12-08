from random import choice
import time
import numpy as np
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Team:
    def __init__(self, name, types, moves, EVs, health='==================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20
        self.pokemons = list()

    def remove_pokemon(self, name):
        foundpokemon = False
        for pokemon in self.pokemons:
            if pokemon.name == name:
                self.pokemons.remove(pokemon)
                foundpokemon = True
        if not foundpokemon:
            return 0

    def add_pokemon(self, pokemon):
        """Add pokemon object to self.pokemons."""
        self.pokemons.append(pokemon)
    
    def revive_pokemons(self, health=100):
        for pokemon in self.pokemons:
            pokemon.current_health = pokemon.starting_health
            print(f"{pokemon.name} is revived.")
    
    def fight(self, other_team):
        for pokemon in self.pokemons: 
            self.name = pokemon.name
        
        print("-----POKEMONE BATTLE-----")
        print("Pokemon 1:", self.name)
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print("Pokemon 2:", other_team.name)
        print("TYPE/", other_team.types)
        print("ATTACK/", other_team.attack)
        print("DEFENSE/", other_team.defense)
        print("LVL/", 3*(1+np.mean([other_team.attack,other_team.defense])))

        time.sleep(2)

        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                if other_team.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                if other_team.types == version[(i+1)%3]:
                    other_team.attack *= 2
                    other_team.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                if other_team.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    other_team.attack /= 2
                    other_team.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        
        
        while (self.bars > 0) and (other_team.bars > 0):
            print(self.name ,"health:", self.health)
            print(other_team.name ,"health:", other_team.health)

            print("Go", {self.name}, "!")
            for i, x in enumerate(self.moves):
                print(i+1, x)
            index = int(input('Pick a move: '))
            print(self.name ,"used", self.moves[index-1])
            time.sleep(1)
            delay_print(string_1_attack)

            other_team.bars -= self.attack
            other_team.health = ""

            for j in range(int(other_team.bars+.1*other_team.defense)):
                other_team.health += "="

            time.sleep(1)
            print(self.name ,"health:", self.health)
            print(other_team.name ,"health:", other_team.health)
            time.sleep(.5)

            if other_team.bars <= 0:
                delay_print("\n..." + other_team.name + ' fainted.')
                break

            print("Go",  other_team.name, "!")
            for i, x in enumerate(other_team.moves):
                print(i+1, x)
            index = int(input('Pick a move: '))
            print(other_team.name ,"used", other_team.moves[index-1])
            time.sleep(1)
            delay_print(string_2_attack)

            self.bars -= other_team.attack
            self.health = ""

            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(self.name ,"health:", self.health)
            print(other_team.name ,"health:", other_team.health)
            time.sleep(.5)

            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break

    