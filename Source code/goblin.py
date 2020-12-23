import random

class WealthGoblin:  # Wealth goblin class
    def __init__(self, min_percent_range, max_percent_range, min_coins_range, max_coins_range):
        self.percentage = random.randrange(min_percent_range, max_percent_range + 1)  # Initialise random percentage value which range depends on the difficulty of the game
        self.coins = random.randrange(min_coins_range, max_coins_range)  # Initialise random coins value which range depends on the difficulty of the game


class HealthGoblin:
    def __init__(self, min_percent_range, max_percent_range, min_health_range, max_health_range):
        self.percentage = random.randrange(min_percent_range, max_percent_range + 1)  # Initialise random percentage value which range depends on the difficulty of the game
        self.health = random.randrange(min_health_range, max_health_range)  # Initialise random health value which range depends on the difficulty of the game


class GamerGoblin:
    def __init__(self, min_coins_range, max_coins_range, min_health_range, max_health_range):
        self.coins = random.randrange(min_coins_range, max_coins_range)  # Initialise random coins value which range depends on the difficulty of the game
        self.health = random.randrange(min_health_range, max_health_range)  # Initialise random health value which range depends on the difficulty of the game
