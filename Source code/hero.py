from getch1 import *
import random


class Hero:
    def __init__(self, hero_coordx, hero_coordy):
        self._coordX = hero_coordx
        self._coordY = hero_coordy
        self._message = ""
        self.health = 100
        self.coins = 1000  # gold coins the hero have.

    def move(self, input_coordX, input_coordY, ch2):  # Takes players keyboard input and adjust heroes coordinates depending on the input
        self._coordY = input_coordY
        self._coordX = input_coordX

        if ch2 == b'w' or ch2 == "w":  # If the players input is W, increment heroes Y coordinate

            self._coordY -= 1
            self._message = "The hero moved towards the north"  # the up arrow key was pressed


        elif ch2 == b's' or ch2 == "s":  # If the players input is S, decrement heroes Y coordinate
            self._coordY += 1
            self._message = "The hero moved towards the south"  # the down arrow key was pressed


        elif ch2 == b'a' or ch2 == "a":  # If the players input is A, decrement heroes X coordinate
            self._coordX -= 1
            self._message = "The hero moved toward the west"  # the left arrow key was pressed

        elif ch2 == b'd' or ch2 == "d":  # If the players input is D, increment heroes X coordinate
            self._coordX += 1
            self._message = "The hero moved toward the east"  # the right arrow key was pressed

        return self._coordX, self._coordY, self._message  # Returns heroes coordinates and corresponding message


    def fight(self, encounter_type, abilities, fight_coordx, fight_coordy, hero_coins, hero_health):
        for i in range(5):
            if encounter_type[i] == 35 and self._coordX == fight_coordy[i] and self._coordY == fight_coordx[i]:
                steal = abilities[i][2]
                percentage = abilities[i][0]
                if not fight_percent_calculator(percentage):
                    print("You fought the Thief Monster and lost " + str(steal) + " coins")
                    hero_coins -= steal
                    return hero_coins, hero_health
                else:
                    print("You have defeated the Thief Monster!")
                    return hero_coins, hero_health

            elif encounter_type[i] == 36 and self._coordX == fight_coordy[i] and self._coordY == fight_coordx[i]:
                damage = abilities[i][1]
                percentage = abilities[i][0]
                if not fight_percent_calculator(percentage):
                    print("You fought the Fighter Monster and lost " + str(damage) + " health")
                    hero_health -= damage
                    return hero_coins, hero_health
                else:
                    print("You have defeated the Fighter Monster!")
                    return hero_coins, hero_health

            elif encounter_type[i] == 37 and self._coordX == fight_coordy[i] and self._coordY == fight_coordx[i]:
                print("You encountered the Gamer Monster and challenged it to a game of rock, paper and scissors!")
                print("Press 'R', 'P', 'S' on your keyboard to choose your option")
                steal = abilities[i][2]
                damage = abilities[i][1]
                if not rock_paper_scissors():
                    print("You fought the Gamer Monster and lost " + str(steal) + " coins and " + str(damage) + " health")
                    hero_coins -= steal
                    hero_health -= damage
                    return hero_coins, hero_health
                else:
                    print("You have defeated the Gamer Monster!")
                    return hero_coins, hero_health


            elif encounter_type[i] == 45 and self._coordX == fight_coordy[i] and self._coordY == fight_coordx[i]:
                percentage = abilities[i][0]
                coins = abilities[i][2]
                if fight_percent_calculator(percentage):
                    print("You have encountered the Wealth Goblin and it gave you " + str(coins) + " coins!")
                    hero_coins += coins
                    return hero_coins, hero_health
                else:
                    print("You have encountered the Wealth Goblin and unfortunately you did not receive anything...")
                    return hero_coins, hero_health

            elif encounter_type[i] == 46 and self._coordX == fight_coordy[i] and self._coordY == fight_coordx[i]:
                percentage = abilities[i][0]
                health = abilities[i][1]
                if fight_percent_calculator(percentage):
                    print("You have encountered the Health Goblin and it restored " + str(health) + " health points!")
                    hero_health += health
                    return hero_coins, hero_health
                else:
                    print("You have encountered the Health Goblin and unfortunately you did not receive anything...")
                    return hero_coins, hero_health

            elif encounter_type[i] == 47 and self._coordX == fight_coordy[i] and self._coordY == fight_coordx[i]:
                print("You encountered the Gamer Goblin and challenged it to a game of rock, paper and scissors!")
                print("Press 'R', 'P', 'S' on your keyboard to choose your option")
                health = abilities[i][1]
                coins = abilities[i][2]
                if rock_paper_scissors():
                    print("You played against the Gamer Monster and won " + str(coins) + " coins got restored " + str(health) + " health")
                    hero_coins += coins
                    hero_health += health
                    return hero_coins, hero_health
                else:
                    print("You lost the game and did not receive anything...")
                    return hero_coins, hero_health


def fight_percent_calculator(percentage):  # Function that is responsible to determine a result of a interactions between hero and monster/goblin
    win_percentage = 100 - percentage
    players_chance = random.randrange(1, 101)

    if win_percentage >= players_chance:  # If the random generated number is less than the percent of the monster/goblin, the hero wins, else loses
        return True
    else:
        return False


def rock_paper_scissors():  # Function that is responsible for the rock, paper and scissors game
    choice = getch()  # Takes the players keyboard input
    computer_choice = 0

    if choice != b'r' and choice != b'p' and choice != b's':  # Checks if the keyboard input is valid
        print("Invalid input, try again")
        return rock_paper_scissors()

    computer = random.randrange(3)  # Generates a random input for the goblin/monster

    if computer == 0:  # Assigns monster's/goblin's input to a string for clearance
        computer_choice = "r"

    elif computer == 1:
        computer_choice = "p"

    elif computer == 2:
        computer_choice = "s"

    #  Finds the correct outcome of the rock, paper and scissors game:
    if (computer_choice == "r" and choice == b'r') or (computer_choice == "p" and choice == b'p') or (
            computer_choice == "s" and choice == b's'):
        print("Its a draw! Pick again")
        return rock_paper_scissors()

    elif computer_choice == "r" and choice == b'p':
        print("You opponent picked rock. You won!")
        return True

    elif computer_choice == "p" and choice == b's':
        print("You opponent picked paper. You won!")
        return True

    elif computer_choice == "s" and choice == b'r':
        print("You opponent picked scissors. You won!")
        return True

    elif computer_choice == "p" and choice == b'r':
        print("You opponent picked paper. You lost. ")
        return False

    elif computer_choice == "s" and choice == b'p':
        print("You opponent picked scissors. You lost.")
        return False

    elif computer_choice == "r" and choice == b's':
        print("You opponent picked rock. You lost.")
        return False
