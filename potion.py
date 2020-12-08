import random

class Potion:
    def __init__(self, name, max_health):
        self.name = name
        self.max_health = max_health

    def heal(self):
        random_health_value = random.randint(0, int(self.max_health))
        return random_health_value
