'''
Maze generation script

Arguments are passed through command-line prompts

For other configuration, see `config.py`

TODO:
- send maze to Minecraft datapack
- add more maze types
'''

import copy
import random

from classes import *

def sendMazeToMinecraft():
  with open("maze/maze.json") as mazeFile, open("maze/mazeworld/datapacks/maze/data/maze/functions/run_maze.mcfunction", 'w') as mazeFunctionFile:
    encodedMaze = json.load(mazeFile)


def generateRectangularMaze(width, height):
  maze = Maze(width,height)

  pastPathPoints = set()

  head = copy.deepcopy(maze.start)
  maze.setValue(head, air)
  pastPathPoints.add(head)

  foundEnd = False
  deadEndsHit = 0
  while deadEndsHit < density*maze.width*maze.height:
    possibleNextHeads = set()
    for direction in directions:
      look = copy.deepcopy(head)
      look.move(direction)
      if maze.getValue(look) == wall: possibleNextHeads.add(look)

    viableNextHeads = set()
    for possibleNextHead in possibleNextHeads:
      numPathNear = 0
      for direction in directions:
        look2 = copy.deepcopy(possibleNextHead)
        look2.move(direction)
        if maze.getValue(look2) == air: numPathNear = numPathNear + 1
      if numPathNear == 1: viableNextHeads.add(possibleNextHead)

    if len(viableNextHeads) == 0:
      deadEndsHit = deadEndsHit + 1
      head = random.choice(list(pastPathPoints))
      continue

    head = random.choice(list(viableNextHeads))
    maze.setValue(head, air)
    if (head.x < maze.height - 4) and (head.y < maze.height - 4): pastPathPoints.add(head)

    if head == maze.end:
      foundEnd = True
      head = random.choice(list(pastPathPoints))

  return maze, foundEnd

def main():
  print(" -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
  print("| Welcome to Finn's Minecraft Maze Generator |")
  print(" -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
  while True:
    mazetype = input("Type of maze (square: 's', rectangle 'r'): ")
    if (mazetype == "s"):
      width_str = input("Sidelength: ")
      while True:
        try: width = abs(int(width_str))
        except:
          print("Sidelength must be an integer value")
          width_str = input("Sidelength: ")
        else:
          height = width
          break
      break
    elif (mazetype == "r"):
      width_str = input("Width: ")
      while True:
        try: width = abs(int(width_str))
        except:
          print("Width must be an integer value")
          width_str = input("Width: ")
        else: break
      height_str = input("Height: ")
      while True:
        try: height = abs(int(height_str))
        except:
          print("Height must be an integer value")
          height_str = input("Height: ")
        else: break
      break
    else: print("Must put either 's' or 'r'")

  print("Generating maze...")
  while True:
    maze, foundEnd = generateRectangularMaze(width=width, height=height)
    if foundEnd: break

  maze.draw()
  maze.encode()

  sendMazeToMinecraft()

if __name__ == "__main__": main()
