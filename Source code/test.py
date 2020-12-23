def load():

    text_list = []
    maze = []

    file = open("SaveFile.txt").read()

    for line in file.split("\n"):
        print(line)

    for line in file.split():
        print(line)


load()


'''
    def save(self, maze):

        save = open("SaveFile.txt", "w")
        for row in maze:
            row_str = str(row).translate({ord(i): None for i in '[,]'})
            save.write(row_str)
            save.write("\n")


        save.write(str(self.game_difficulty) + "\n")
        save.write(str(self.hero_coordx) + " " + str(self.hero_coordy) + "\n")
        save.write(str(self.health) + " " + str(self.coins) + "\n")

        save.write(str(self.monsters_visited).translate({ord(i): None for i in "{','}"}) + "\n")
        save.write(str(self.monster_coordx).translate({ord(i): None for i in '[,]'}) + "\n")
        save.write(str(self.monster_coordy).translate({ord(i): None for i in '[,]'}) + "\n")
        save.write(str(self.monster_type).translate({ord(i): None for i in '[,]'}) + "\n")
        save.write(str(self.monster_abilities).translate({ord(i): None for i in '[,]'}) + "\n")

        save.write(str(self.goblin_coordx).translate({ord(i): None for i in '[,]'}) + "\n")
        save.write(str(self.goblin_coordy).translate({ord(i): None for i in '[,]'}) + "\n")
        save.write(str(self.goblin_type).translate({ord(i): None for i in '[,]'}) + "\n")
        save.write(str(self.goblin_abilities).translate({ord(i): None for i in '[,]'}))
        
    def load(self):

        text_list = []
        index = 0

        file = open("SaveFile.txt").read()

        file = file.replace("\n", " ")

        for line in file.split(" "):
            text_list.append(line)

        for i in range(17):
            for j in range(17):
                self.maze[i][j] = text_list[index]
                index += 1

        
        
'''