#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Version: 1.0

import random

class ThiefMonster:  # Thief monster class
    def __init__(self, min_percent_range, max_percent_range, min_steal_range, max_steal_range):
        self.percentage = random.randrange(min_percent_range, max_percent_range + 1)  # Initialise random percentage value which range depends on the difficulty of the game
        self.steal = random.randrange(min_steal_range, max_steal_range + 1)  # Initialise random steal value which range depends on the difficulty of the game


class FighterMonster:  # Fighter monster class
    def __init__(self, min_percent_range, max_percent_range, min_damage_range, max_damage_range):
        self.percentage = random.randrange(min_percent_range, max_percent_range + 1)   # Initialise random percentage value which range depends on the difficulty of the game
        self.damage = random.randrange(min_damage_range, max_damage_range + 1)  # Initialise random damage value which range depends on the difficulty of the game


class GamerMonster:  # Gamer monster class
    def __init__(self, min_steal_range, max_steal_range, min_damage_range, max_damage_range):
        self.steal = random.randrange(min_steal_range, max_steal_range + 1)  # Initialise random steal value which range depends on the difficulty of the game
        self.damage = random.randrange(min_damage_range, max_damage_range + 1)  # Initialise random damage value which range depends on the difficulty of the game
