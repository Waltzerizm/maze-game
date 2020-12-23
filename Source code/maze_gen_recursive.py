# This code is based on http://arcade.academy/examples/maze_recursive.html
#
# Modified by CS1527 Course Team on 30 January 2019
#
#

import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

TILE_EMPTY = 0
TILE_CRATE = 1

# Maze must have an ODD number of rows and columns.
# Walls go on EVEN rows/columns.
# Openings go on ODD rows/columns
MAZE_HEIGHT = 51
MAZE_WIDTH = 51


def create_empty_grid(width, height, default_value=TILE_EMPTY):
    """ Create an empty grid. """
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            grid[row].append(default_value)
    return grid


def create_outside_walls(maze):
    """ Create outside border walls."""

    # Create left and right walls
    for row in range(len(maze)):
        maze[row][0] = TILE_CRATE
        maze[row][len(maze[row]) - 1] = TILE_CRATE

    # Create top and bottom walls
    for column in range(1, len(maze[0]) - 1):
        maze[0][column] = TILE_CRATE
        maze[len(maze) - 1][column] = TILE_CRATE


def make_maze_recursive_call(maze, top, bottom, left, right):
    """
    Recursive function to divide up the maze in four sections
    and create three gaps.
    Walls can only go on even numbered rows/columns.
    Gaps can only go on odd numbered rows/columns.
    Maze must have an ODD number of rows and columns.
    """

    # Figure out where to divide horizontally
    start_range = bottom + 2
    end_range = top - 1
    y = random.randrange(start_range, end_range, 2)

    # Do the division
    for column in range(left + 1, right):
        maze[y][column] = TILE_CRATE

    # Figure out where to divide vertically
    start_range = left + 2
    end_range = right - 1
    x = random.randrange(start_range, end_range, 2)

    # Do the division
    for row in range(bottom + 1, top):
        maze[row][x] = TILE_CRATE

    # Now we'll make a gap on 3 of the 4 walls.
    # Figure out which wall does NOT get a gap.
    wall = random.randrange(4)
    if wall != 0:
        gap = random.randrange(left + 1, x, 2)
        maze[y][gap] = TILE_EMPTY

    if wall != 1:
        gap = random.randrange(x + 1, right, 2)
        maze[y][gap] = TILE_EMPTY

    if wall != 2:
        gap = random.randrange(bottom + 1, y, 2)
        maze[gap][x] = TILE_EMPTY

    if wall != 3:
        gap = random.randrange(y + 1, top, 2)
        maze[gap][x] = TILE_EMPTY

    # If there's enough space, to a recursive call.
    if top > y + 3 and x > left + 3:
        make_maze_recursive_call(maze, top, y, left, x)

    if top > y + 3 and x + 3 < right:
        make_maze_recursive_call(maze, top, y, x, right)

    if bottom + 3 < y and x + 3 < right:
        make_maze_recursive_call(maze, y, bottom, x, right)

    if bottom + 3 < y and x > left + 3:
        make_maze_recursive_call(maze, y, bottom, left, x)


def make_maze_recursion(maze_width, maze_height):
    """ Make the maze by recursively splitting it into four rooms. """
    maze = create_empty_grid(maze_width, maze_height)
    # Fill in the outside walls
    create_outside_walls(maze)

    # Start the recursive process
    make_maze_recursive_call(maze, maze_height - 1, 0, 0, maze_width - 1)
    maze, coordx, coordy, m_coordx, m_coordy, g_coordx, g_coordy = print_maze_hero_monster(maze, 17, 17, 0, 2, 3, 4)
    return maze, coordx, coordy, m_coordx, m_coordy, g_coordx, g_coordy


def print_maze(maze, wall="#", space="-"):
    """print out the maze in the terminal"""
    for row in maze:
        row_str = str(row)
        row_str = row_str.replace("1", wall)  # replace the wall character
        row_str = row_str.replace("0", space)  # replace the space character
        print("".join(row_str))


def print_maze_hero_monster(maze, maze_width, maze_height, space=0, hero=2, monster=3, goblin=4):  # Function that initialises the hero, 5 monsters and 5 goblins on the map
    m_coordx = [0, 0, 0, 0, 0]
    m_coordy = [0, 0, 0, 0, 0]
    g_coordx = [0, 0, 0, 0, 0]
    g_coordy = [0, 0, 0, 0, 0]

    maze, coordx, coordy = character_generator(maze, maze_width, maze_height, hero, space)  # Creates a hero in the maze

    maze, m_coordx[0], m_coordy[0] = character_generator(maze, maze_width, maze_height, monster * 10 + 5, space)  # Creates a Thief monster in the maze
    maze, m_coordx[1], m_coordy[1] = character_generator(maze, maze_width, maze_height, monster * 10 + 6, space)  # Creates a Fighter monster in the maze
    maze, m_coordx[2], m_coordy[2] = character_generator(maze, maze_width, maze_height, monster * 10 + 7, space)  # Creates a Gamer monster in the maze

    maze, g_coordx[0], g_coordy[0] = character_generator(maze, maze_width, maze_height, goblin * 10 + 5, space)  # Creates a Wealth goblin in the maze
    maze, g_coordx[1], g_coordy[1] = character_generator(maze, maze_width, maze_height, goblin * 10 + 6, space)  # Creates a Health goblin in the maze
    maze, g_coordx[2], g_coordy[2] = character_generator(maze, maze_width, maze_height, goblin * 10 + 7, space)  # Creates a Gamer goblin in the maze

    for i in range(2):  # Creates the rest of 2 monsters/goblins of random type
        maze, m_coordx[i+3], m_coordy[i+3] = character_generator(maze, maze_width, maze_height, monster * 10 + random.randrange(5, 8, 1), space)
        maze, g_coordx[i+3], g_coordy[i+3] = character_generator(maze, maze_width, maze_height, goblin * 10 + random.randrange(5, 8, 1), space)

    return maze, coordx, coordy, m_coordx, m_coordy, g_coordx, g_coordy


def character_generator(maze, maze_width, maze_height, character, space):  # Function that creates an entity on the map
    coordx = random.randrange(1, maze_height, 1)
    coordy = random.randrange(1, maze_width, 1)

    while maze[coordx][coordy] != character:  # If the place is not occupied place an entity else generate new coordinates
        if maze[coordx][coordy] != space:
            coordx = random.randrange(1, maze_height, 1)
            coordy = random.randrange(1, maze_width, 1)
        else:
            maze[coordx][coordy] = character
            break

    return maze, coordx, coordy
