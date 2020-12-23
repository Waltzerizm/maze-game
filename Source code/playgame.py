from copy import deepcopy
from hero import Hero
from maze_gen_recursive import make_maze_recursion
from monster import ThiefMonster, FighterMonster, GamerMonster
from goblin import WealthGoblin, HealthGoblin, GamerGoblin
from getch1 import *
import pickle
import sys
import time

# --------------------Global variables`

WALL_CHAR = "■"
SPACE_CHAR = " "
HERO_CHAR = "H"
MONSTER_CHAR = "M"
GOBLIN_CHAR = "G"

#--------------------Environment class that is used to create and manipulate the game's settings------------------------

class _Environment:
    """Environment includes Maze+Monster+Goblin"""

    def __init__(self, maze):  # The constructor initializes the maze that we generate in the maze_gen_recursive.py
        self._environment = deepcopy(maze)


    def set_coord(self, x, y, val):  # Function that is used to set a value in a certain place in the maze
        self._environment[x][y] = val


    def get_coord(self, x, y):  # Function that is used to retrieve a certain value from the maze
        return self._environment[x][y]


    def print_environment(self):  # Function that iterates trough all the values in the maze, replaces them with the right string form and prints back the new value to the user
        """print out the environment in the terminal"""
        for row in self._environment:
            row_str = str(row)
            row_str = row_str.replace("1", WALL_CHAR)  # replace the wall character
            row_str = row_str.replace("0", SPACE_CHAR)  # replace the space character
            row_str = row_str.replace("2", HERO_CHAR)  # replace the hero character

            # replaces the monster character---------------
            row_str = row_str.replace("35", MONSTER_CHAR)
            row_str = row_str.replace("36", MONSTER_CHAR)
            row_str = row_str.replace("37", MONSTER_CHAR)

            # replaces the goblin character---------------
            row_str = row_str.replace("45", GOBLIN_CHAR)
            row_str = row_str.replace("46", GOBLIN_CHAR)
            row_str = row_str.replace("47", GOBLIN_CHAR)

            # replace certain characters to make the maze look nicer---------------
            row_str = row_str.replace(",", "")
            row_str = row_str.replace("]", "")
            row_str = row_str.replace("[", "")

            print("".join(row_str))


    def game_difficulty(self, player_input):  # Function that takes the player input and assigns the corresponding difficulty
        if player_input == b'1' or player_input == "1":  # If easy difficulty has been selected, all the different monster and goblin classes are called with certain values
            difficulty = 1

            TM = ThiefMonster(1, 25, 50, 100)
            FM = FighterMonster(1, 25, 1, 10)
            GM = GamerMonster(50, 100, 1, 10)

            WG = WealthGoblin(1, 25, 50, 100)
            HG = HealthGoblin(1, 25, 1, 10)
            GG = GamerGoblin(50, 100, 1, 10)

            return difficulty, TM, FM, GM, WG, HG, GG

        elif player_input == b'2' or player_input == "2":  # If medium difficulty has been selected, all the different monster and goblin classes are called with certain values
            difficulty = 2

            TM = ThiefMonster(25, 50, 100, 200)
            FM = FighterMonster(25, 50, 10, 20)
            GM = GamerMonster(100, 200, 10, 20)

            WG = WealthGoblin(25, 50, 100, 200)
            HG = HealthGoblin(25, 50, 10, 20)
            GG = GamerGoblin(100, 200, 10, 20)

            return difficulty, TM, FM, GM, WG, HG, GG

        elif player_input == b'3' or player_input == "3":  # If hard difficulty has been selected, all the different monster and goblin classes are called with certain values
            difficulty = 3

            TM = ThiefMonster(50, 75, 200, 300)
            FM = FighterMonster(50, 75, 20, 30)
            GM = GamerMonster(200, 300, 20, 30)

            WG = WealthGoblin(50, 75, 200, 300)
            HG = HealthGoblin(50, 75, 20, 30)
            GG = GamerGoblin(200, 300, 20, 30)

            return difficulty, TM, FM, GM, WG, HG, GG

        elif player_input == b'4' or player_input == "4":  # If very hard difficulty has been selected, all the different monster and goblin classes are called with certain values
            difficulty = 4

            TM = ThiefMonster(75, 100, 300, 500)
            FM = FighterMonster(75, 100, 30, 50)
            GM = GamerMonster(300, 500, 30, 50)

            WG = WealthGoblin(75, 100, 300, 400)
            HG = HealthGoblin(75, 100, 30, 50)
            GG = GamerGoblin(300, 500, 30, 50)

            return difficulty, TM, FM, GM, WG, HG, GG


    def monster_initialisation(self, player_input, monster_list, goblin_list):  # Function that set all the monster's and goblin's abilities for the game
        monster_percent_damage_steal_value = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        goblin_percent_health_coin_value = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        difficulty = 0

        for i in range(5):
            difficulty, TM, FM, GM, WG, HG, GG = self.game_difficulty(player_input)  # Retrieves the right classes attributes that are set by the difficulty of the game

            if monster_list[i] == 35:  # Sets the percentage and steal value for the thief monster
                monster_percent_damage_steal_value[i][0] = TM.percentage
                monster_percent_damage_steal_value[i][2] = TM.steal

            elif monster_list[i] == 36:  # Sets the percentage and damage value for the fight monster
                monster_percent_damage_steal_value[i][0] = FM.percentage
                monster_percent_damage_steal_value[i][1] = FM.damage

            elif monster_list[i] == 37:  # Sets the damage and steal value for the gamer monster
                monster_percent_damage_steal_value[i][1] = GM.damage
                monster_percent_damage_steal_value[i][2] = GM.steal

            if goblin_list[i] == 45:  # Sets the percentage and coin value for the wealth monster
                goblin_percent_health_coin_value[i][0] = WG.percentage
                goblin_percent_health_coin_value[i][2] = WG.coins

            elif goblin_list[i] == 46:  # Set the percentage and health value for the health monster
                goblin_percent_health_coin_value[i][0] = HG.percentage
                goblin_percent_health_coin_value[i][1] = HG.health

            elif goblin_list[i] == 47:  # Set the health and coin value for the gamer monster
                goblin_percent_health_coin_value[i][1] = GG.health
                goblin_percent_health_coin_value[i][2] = GG.coins

        return difficulty, monster_percent_damage_steal_value, goblin_percent_health_coin_value  # Return the difficulty the player has selected and the monster/goblin ability values


    # Function that prints out coordinates of the hero, and coordinates/type/attributes of the monster/goblin
    def every_position_print(self, hero_coordy, hero_coordx, monster_coordx, monster_coordy, goblin_coordx, goblin_coordy, monster_abilities, goblin_abilities):
        monster_name = ""
        goblin_name = ""
        monster_ability = ""
        goblin_ability = ""

        print("Hero's coordinates are: " + str(hero_coordy) + " " + str(hero_coordx))
        print("")
        print("Monster coordinates are: ")

        for i in range(5):  #  Loops trough monsters and prints their coordinates, type and attributes
            monster_type = self.get_coord(monster_coordx[i], monster_coordy[i])

            if monster_type == 35:
                monster_name = "Thief Monster"
                monster_ability = "(" + str(monster_abilities[i][0]) + "% " + str(monster_abilities[i][2]) + ")"

            elif monster_type == 36:
                monster_name = "Fighter Monster"
                monster_ability = "(" + str(monster_abilities[i][0]) + "% " + str(monster_abilities[i][1]) + ")"

            elif monster_type == 37:
                monster_name = "Gamer Monster"
                monster_ability = "(" + str(monster_abilities[i][2]) + " " + str(monster_abilities[i][1]) + ")"

            print(str(monster_name) + " with abilities " + monster_ability + " is at " + str(monster_coordy[i]) + " " + str(monster_coordx[i]))

        print("")
        print("")
        print("Goblin coordinates are: ")

        for i in range(5):  #  Loops trough goblins and prints their coordinates, type and attributes
            goblin_type = self.get_coord(goblin_coordx[i], goblin_coordy[i])

            if goblin_type == 45:
                goblin_name = "Wealth Goblin"
                goblin_ability = "(" + str(100 - goblin_abilities[i][0]) + "% " + str(goblin_abilities[i][2]) + ")"

            elif goblin_type == 46:
                goblin_name = "Health Goblin"
                goblin_ability = "(" + str(100 - goblin_abilities[i][0]) + "% " + str(goblin_abilities[i][1]) + ")"

            elif goblin_type == 47:
                goblin_name = "Gamer Goblin"
                goblin_ability = "(" + str(goblin_abilities[i][2]) + " " + str(goblin_abilities[i][1]) + ")"

            print(str(goblin_name) + " with abilities " + goblin_ability + " is at " + str(goblin_coordy[i]) + " " + str(goblin_coordx[i]))


    def monster_position_check(self, monster_coordx, monster_coordy, monster_types):  # Function that makes sure the monsters do not disappear after interacting with the hero
        for i in range(5):
            if self.get_coord(monster_coordx[i], monster_coordy[i]) == 0:  # If the value in the monster's position is 0 after the hero steps off, the value is replaced by the certain monsters value
                self.set_coord(monster_coordx[i], monster_coordy[i], monster_types[i])


    def visit(self, monster_coordx, monster_coordy, places):  # Function that handles the set, which is responsible for tracking what monsters the hero has encountered
        for i in range(5):
            coord = str(monster_coordx[i]) + ", " + str(monster_coordy[i])
            if self.get_coord(monster_coordx[i], monster_coordy[i]) == 2:  # If the hero encountered the monster, it's coordinates are added to the list
                places.add(coord)

        return places  # Returns a set of monster coordinates the hero has visited

#-----------------------------------------------------------------------------------------------------------------------


#---------------Game class that is used initialise the game and manipulate it depending on the players input------------
class Game:
    _count = 0

    # ---------------------------------------------------------------

    def __init__(self):

        # -----------------------Game

        self.maze, self.hero_coordy, self.hero_coordx, self.monster_coordx, self.monster_coordy, self.goblin_coordx, self.goblin_coordy = make_maze_recursion(17, 17)  # we retrieve the coordinated of hero/monsters/goblin
        self.MyEnvironment = _Environment(self.maze)  # initial environment is the maze itself
        self.game_difficulty = ""
        self._count = 0
        self.message = ""
        self.player_name = ""

        #-----------------------Monsters/Goblins

        self.monster_type = []
        self.goblin_type = []

        for i in range(5):  # Loop trough monsters/goblin coordinates and retrieve all the types that are in the current game
            self.monster_type.append(self.MyEnvironment.get_coord(self.monster_coordx[i], self.monster_coordy[i]))
            self.goblin_type.append(self.MyEnvironment.get_coord(self.goblin_coordx[i], self.goblin_coordy[i]))

        self.monster_abilities = []
        self.goblin_abilities = []

        #-----------------------Hero

        self.myHero = Hero(self.hero_coordx, self.hero_coordy)  # Initialise the hero from hero.py
        self.hero_old_coordx = 0
        self.hero_old_coordy = 0
        self.monsters_visited = set()
        self.coins = self.myHero.coins  # Receive the coins value from hero.py
        self.health = self.myHero.health  # Receive the heath value from hero.py
    # ---------------------------------------------------------------

    def game_functions(self, player_input):  # Function that handles the flow of other functions that interact with the game if the player input is W, A, S or D
        self.hero_old_coordx = self.hero_coordx  # Saves the last coordinates of the hero
        self.hero_old_coordy = self.hero_coordy
        self._count += 1
        self.hero_coordx, self.hero_coordy, self.message = self.myHero.move(self.hero_coordx, self.hero_coordy, player_input)  # Calls the function that handles the heroes movement in the maze
        self.hero_coordx, self.hero_coordy, self._count, self.health = self.wall_check(
            self.hero_coordx, self.hero_coordy, self.hero_old_coordx, self.hero_old_coordy, self.health,
            self._count, self.message)  # Calls the function that checks if the players next movement is not directed into a wall

        self.MyEnvironment.monster_position_check(self.monster_coordx, self.monster_coordy, self.monster_type)  # Calls the function that makes sure the monsters never disappear

        self.monsters_visited = self.MyEnvironment.visit(self.monster_coordx, self.monster_coordy, self.monsters_visited)  # Calls the function which record which monsters the hero has encountered

        self.goblin_coordx, self.goblin_coordy, self.goblin_type, self.coins, self.health = encounter(
            self.monster_coordx, self.monster_coordy, self.monster_abilities, self.goblin_coordx, self.goblin_coordy,
            self.goblin_abilities,
            self.hero_coordx, self.hero_coordy, self.monster_type, self.goblin_type, self.coins, self.health)  # Calls the function that handles the encounter with the monster/goblin


    def game_controls(self, player_input):  # Function that handles the players input from the keyboard

        if player_input == b'w' or player_input == b'a' or player_input == b's' or player_input == b'd' or \
                player_input == "w" or player_input == "a" or player_input == "s" or player_input == "d":  #  If player's keyboard input is W, A, S or D the function regarding that input is called

            self.game_functions(player_input)

        elif player_input == b'1' or player_input == b'2' or player_input == b'3' or player_input == b'4' or \
                player_input == "1" or player_input == "2" or player_input == "3" or player_input == "4":  # Else if the players input is 1, 2, 3 or 4 the corresponding difficulty is selected and message is printed to announce what difficulty has been chosen

            self.game_difficulty, self.monster_abilities, self.goblin_abilities = self.MyEnvironment.monster_initialisation(
                player_input, self.monster_type, self.goblin_type)

            print("")
            if player_input == b'1' or player_input == "1":
                print("Easy difficulty has been selected")
            elif player_input == b'2' or player_input == "2":
                print("Medium difficulty has been selected")
            elif player_input == b'3' or player_input == "3":
                print("Hard difficulty has been selected")
            elif player_input == b'4' or player_input == "4":
                print("Very hard difficulty has been selected")
            print("")



        elif player_input == b'h' or player_input == "h":  # Else if the player input is H, then the control manual is printed
            print("Hero movement controls: W - up, A - left, S - down, D - right")
            print("K - saves the game")
            print("L - loads the saved game")
            print("M - refreshes the map/shows the position of the hero and positions, attributes of all monsters and goblins")
            print("X - saves and closes the game")

        elif player_input == b'm' or player_input == "m":  # Else if the player input is M, then the function prints the coordinates of the hero and the coordinates of monsters/goblins
            self.MyEnvironment.every_position_print(self.hero_coordx, self.hero_coordy, self.monster_coordx, self.monster_coordy, self.goblin_coordx, self.goblin_coordy, self.monster_abilities, self.goblin_abilities)


        elif player_input == b'k' or player_input == "k":  # Else if the players input is K, the game progress is saved
            self.save()
            print("The game has been saved")
            print("")

        elif player_input == b'l' or player_input == "l":  # Else if the players input is L, the saved game progress is loaded
            self.load()
            print("The saved game has been loaded")
            print("")

        elif player_input == b'x' or player_input == "x":  # Else if the player input is X, the game closes and saves
            self.save()
            sys.exit(0)

        else:  # If player's input is not mentioned above, the "Invalid command" is printed
            print("Invalid command")
            return self.game_controls(player_input = getch())

    def wall_check(self, coordX, coordY, old_coordX, old_coordY, health, count, message):  # Function that checks if the heroes next movement is valid (does not let the hero go into/trough walls)
        if self.MyEnvironment.get_coord(coordY, coordX) == 1:  # If heroes next move is directed into a wall, heroes coordinated are set back to its last step
            coordX = old_coordX
            coordY = old_coordY
            self.MyEnvironment.set_coord(coordY, coordX, 2)
            print(message + "\n" + "You can not go there, Hero")  # Prints a message to inform the hero that it hit a wall
        else:  # If heroes next move is an empty space, it moves successfully and loses 1 health
            self.MyEnvironment.set_coord(coordY, coordX, 2)
            print(message)
            self.MyEnvironment.set_coord(old_coordY, old_coordX, 0)
            health -= 1

        return coordX, coordY, count, health  # return the new coordinates and health of the hero


    def cmd_print(self):  # Function that is responsible for printing game/information to the screen
        print("")
        print("Hero health: " + str(self.health) + " Hero loot: " + str(self.coins) + "             Press 'H' for help")
        self.MyEnvironment.print_environment()
        print("============================", self._count)
        print("")

    def win(self):  # Function that is responsible for the output if the hero wins
        print("")
        print("YOU HAVE WON THE GAME!")
        print("Your score is: " + str(self.coins))  # Prints the player's score
        self.player_name = input("Hero, what is your name? ")  # Takes the player's name for the leaderboard
        difficulty_leaderboard(self.player_name, self.coins, self.game_difficulty)  # Puts the name and score of the player into a leaderboard that corresponds to the selected difficulty
        print_leaderboard()  # Prints the leaderboards
        input("Press enter to close the screen")


    def save(self):  # Function that is used for saving the game
        with open('save.pkl', 'wb') as f:  # We use the pickle module for this
            pickle.dump([self.MyEnvironment, self.game_difficulty, self.hero_coordx, self.hero_coordy, self.health, self.coins, self.monsters_visited, self.monster_coordx, self.monster_coordy, self.monster_type, self.monster_abilities, self.goblin_coordx, self.goblin_coordy, self.goblin_type, self.goblin_abilities],f)


    def load(self):  # Function that is used for loading the game
        with open('save.pkl', 'rb') as f:  # We use the pickle module for this
            self.MyEnvironment, self.game_difficulty, self.hero_coordx, self.hero_coordy, self.health, self.coins, self.monsters_visited, self.monster_coordx, self.monster_coordy, self.monster_type, self.monster_abilities, self.goblin_coordx, self.goblin_coordy, self.goblin_type, self.goblin_abilities = pickle.load(f)


    def play(self):  # Function that is responsible starting and playing the game
        print("Player, select game's difficulty: 1 - Easy, 2 - Medium, 3 - Hard, 4 - Very Hard")
        print("Or press 'L' to load the last saved game")

        self.game_controls(player_input=getch())  # Takes the player keyboard input to determine the difficulty

        self.MyEnvironment.every_position_print(self.hero_coordx, self.hero_coordy, self.monster_coordx, self.monster_coordy, self.goblin_coordx, self.goblin_coordy, self.monster_abilities, self.goblin_abilities)  # Prints every entity coordinated

        while True:  # Runs the game until certain status is achieved

            self.cmd_print()  #  Prints the necessary information for the players
            self.game_controls(player_input=getch())  # Handles player keyboard input

            if status(self.health, self.monsters_visited) == "LOSE":  # Checks the status of the game
                lose()  # If the status is "LOSE", the function lose is called and the game is stopped
                break
            elif status(self.health, self.monsters_visited) == "VICTORY":
                self.win()  # If the status is "WIN", the function win is called and the game is stopped
                break

#Static functions------------------------------------------------------------------------------------------------------

def encounter(monster_coordx, monster_coordy, monster_abilities, goblin_coordx, goblin_coordy,  # Function that is responsible for the interactions with monsters/goblins
                goblin_abilities, hero_coordx, hero_coordy, monster_type, goblin_type, hero_coins, hero_health):
    h = Hero(hero_coordx, hero_coordy)

    for i in range(5):  # We loop trough every entity coordinates to checks what did the hero encounter
        if monster_coordy[i] == hero_coordx and monster_coordx[i] == hero_coordy:  # If the hero encountered a monster, certain functions are called
            interaction_pre_information(hero_coordx, hero_coordy, monster_coordx, monster_coordy, goblin_coordx, goblin_coordy, monster_abilities, goblin_abilities, monster_type, goblin_type)  # Display to the player what monster the hero has met and what abilities it has
            hero_coins, hero_health = h.fight(monster_type, monster_abilities, monster_coordx, monster_coordy,
                                                  hero_coins, hero_health)  # Fight function in hero.py is called which return the outcome of the encounter
            break

        elif goblin_coordy[i] == hero_coordx and goblin_coordx[i] == hero_coordy:  # If the hero encountered a goblin, certain functions are called
            interaction_pre_information(hero_coordx, hero_coordy, monster_coordx, monster_coordy, goblin_coordx, goblin_coordy, monster_abilities, goblin_abilities, monster_type, goblin_type)  # Display to the player what goblin the hero has met and what abilities it has
            hero_coins, hero_health = h.fight(goblin_type, goblin_abilities, goblin_coordx, goblin_coordy,
                                                  hero_coins, hero_health)  # Fight function in hero.py is called which return the outcome of the encounter

            goblin_coordx[i] = goblin_coordy[i] = 0  # Removes the goblin from the maze after meeting it
            goblin_type[i] = None
            break

    return goblin_coordx, goblin_coordy, goblin_type, hero_coins, hero_health  # Returns the outcome of the fight and modified goblin coordinates and types list


def print_leaderboard():  # Function that prints the leaderboard of each difficulty
    difficulties = ["LeaderboardEasy.txt", "LeaderboardMedium.txt", "LeaderboardHard.txt", "LeaderboardVeryHard.txt"]
    difficulty_name = ["EASY", "MEDIUM", "HARD", "VERY HARD"]
    index = 0

    print("")
    print("==============LEADERBOARDS==============")

    for difficulty in difficulties:  # Loop trough every difficulties text file and print the content for the player
        print("")
        print("TOP 10 PLAYERS OF THE " + difficulty_name[index] + " DIFFICULTY")
        file = open(difficulty).read()
        for line in file.split("\n"):
            print(line)
        index += 1


def interaction_pre_information(hero_coordx, hero_coordy, monster_coordx, monster_coordy, goblin_coordx, goblin_coordy, monster_abilities, goblin_abilities, monster_type, goblin_type):  # Function that prints what entity the hero has encountered
    message = ""

    print("")
    print("The hero is encountering a ", end="")

    for i in range(5):  # Loops trough every entity coordinated to find the monster/goblin the hero has encountered
        if hero_coordx == monster_coordy[i] and hero_coordy == monster_coordx[i]:  # If the hero has encountered a monster, it's type and abilities will be printed before the fight
            if monster_type[i] == 35:
                message = "Thief Monster with abilities " + "(" + str(monster_abilities[i][0]) + "% " + str(monster_abilities[i][2]) + ")"

            elif monster_type[i] == 36:
                message = "Fighter Monster with abilities " + "(" + str(monster_abilities[i][0]) + "% " + str(monster_abilities[i][1]) + ")"

            elif monster_type[i] == 37:
                message = "Gamer Monster with abilities " + "(" + str(monster_abilities[i][2]) + " " + str(monster_abilities[i][1]) + ")"

        elif hero_coordx == goblin_coordy[i] and hero_coordy == goblin_coordx[i]:  # If the hero has encountered a goblin, it's type and abilities will be printed before the fight
            if goblin_type[i] == 45:
                message = "Wealth Goblin with abilities " + "(" + str(100 - goblin_abilities[i][0]) + "% " + str(goblin_abilities[i][2]) + ")"

            elif goblin_type[i] == 46:
                message = "Health Goblin with abilities " + "(" + str(100 - goblin_abilities[i][0]) + "% " + str(goblin_abilities[i][1]) + ")"

            elif goblin_type[i] == 47:
                message = "Gamer Goblin with abilities " + "(" + str(goblin_abilities[i][2]) + " " + str(goblin_abilities[i][1]) + ")"

    print(message)

    for i in range(4):  # Creates a small delay before the fight so the player has the time to read what kind of monster/goblin the hero is encountering
        for dot in [".  ", ".. ", "..."]:
            print(dot, end="\r")
            time.sleep(0.25)

    print("")

def status(health, places):  # Function that checks if the player has already met the conditions for a lose/victory
    if health <= 0:  # If the health of the hero is below 0, the player loses the game
        return "LOSE"

    if len(places) == 5 and health > 0:  # If the hero has visited all 5 monsters and has more than 0 health, then the player wins the game
        return "VICTORY"


def lose():  # Function that handles the output if the player loses the game
    print("YOU HAVE LOST THE GAME")
    input("Press enter to close the screen")


def difficulty_leaderboard(name, score, difficulty):  # Function that takes the name and score of a victorious player and puts it in certain leaderboard
    file_name = difficulty
    names = []
    scores = []
    text_list = []

    if difficulty == 1:  # Checks what difficulty the player was playing on and selects the corresponding leaderboard
        file_name = "LeaderboardEasy.txt"
    elif difficulty == 2:
        file_name = "LeaderboardMedium.txt"
    elif difficulty == 3:
        file_name = "LeaderboardHard.txt"
    elif difficulty == 4:
        file_name = "LeaderboardVeryHard.txt"

    file = open(file_name, "a")  # Opens the text file and puts the players name and score into it
    file.write("\n" + name + " " + str(score))
    file.close()

    file = open(file_name).read()

    for line in file.split():  # Opens and puts the content of the text file into a list
        text_list.append(line)

    file = open(file_name, "w")

    for i in range(len(text_list)):  # Sorts the text list into names and scores
        if i % 2 != 0:
            scores.append(int(text_list[i]))
        else:
            names.append(text_list[i])

    for i in range(len(names)):  # Sorts the scores and names depending from the size of the score
        for j in range(len(names)):
            if scores[i] > scores[j]:
                scores[i], scores[j] = scores[j], scores[i]
                names[i], names[j] = names[j], names[i]

    if len(names) <= 10:  # Only takes the top 10 scores
        length = len(names)
    else:
        length = 10

    for i in range(length):  # Writes the sorted top 10 score into the text file
        file.write(names[i] + " " + str(scores[i]) + "\n")

    file.close()
#-----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    myGame = Game()
    myGame.play()
