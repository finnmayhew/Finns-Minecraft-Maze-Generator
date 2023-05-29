'''
Maze generation script

Arguments are passed through command-line prompts

For other configuration, see `config.py`
'''

import copy
import random

from classes import *

def sendMazeToMinecraft():
  with open("maze/maze.json") as mazeFile, open("maze/mazeworld/datapacks/maze/data/maze/functions/make_maze.mcfunction", 'w') as mazeFunctionFile:
    encodedMaze = json.load(mazeFile)
    mazeFunctionFile.write("scoreboard players add #maze spawntimer 1\n")
    mazeFunctionFile.write("execute if score #maze spawntimer matches 10 run ")
    mazeFunctionFile.write("spawnpoint @a 23 1 23 -45\n")
    mazeFunctionFile.write("execute if score #maze spawntimer matches 15 run ")
    mazeFunctionFile.write("tp @a 23 1 23 -45 0\n")
    
    for room in encodedMaze["rooms"]:
      x = room["y"]*16
      z = room["x"]*16

      if   room["type"] == "start":
        if   room["orientation"] == 2:
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:start2 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
        elif room["orientation"] == 4:
          x = x + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:start2 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" clockwise_90\n")
        else: # (6)
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:start6 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
      elif room["type"] == "end":
        if   room["orientation"] == 1:
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:end1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
        else: # (8)
          z = z + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:end1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" counterclockwise_90\n")
      elif room["type"] == "edge":
        mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
        mazeFunctionFile.write("place template maze:edge ")
        mazeFunctionFile.write(str(x))
        mazeFunctionFile.write(" 0 ")
        mazeFunctionFile.write(str(z))
        mazeFunctionFile.write("\n")
      elif room["type"] == "wall":
        mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
        mazeFunctionFile.write("place template maze:wall ")
        mazeFunctionFile.write(str(x))
        mazeFunctionFile.write(" 0 ")
        mazeFunctionFile.write(str(z))
        mazeFunctionFile.write("\n")
      elif room["type"] == "deadend":
        if   room["orientation"] == 1:
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:deadend1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
        elif room["orientation"] == 2:
          x = x + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:deadend1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" clockwise_90\n")
        elif room["orientation"] == 4:
          x = x + 15
          z = z + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:deadend1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" 180\n")
        else: # (8)
          z = z + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:deadend1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" counterclockwise_90\n")
      elif room["type"] == "turn":
        if   room["orientation"] == 3:
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:turn3 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
        elif room["orientation"] == 6:
          x = x + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:turn3 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" clockwise_90\n")
        elif room["orientation"] == 9:
          z = z + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:turn3 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" counterclockwise_90\n")
        else: # (12)
          x = x + 15
          z = z + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:turn3 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" 180\n")
      elif room["type"] == "hall":
        if   room["orientation"] == 5:
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:hall5 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
        else: # (10)
          z = z + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:hall5 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" counterclockwise_90\n")
      elif room["type"] == "tee":
        if   room["orientation"] == 7:
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:tee7 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
        elif room["orientation"] == 11:
          z = z + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:tee7 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" clockwise_90\n")
        elif room["orientation"] == 13:
          x = x + 15
          z = z + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:tee7 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" 180\n")
        else: # (14)
          x = x + 15
          mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
          mazeFunctionFile.write("place template maze:tee7 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" clockwise_90\n")
      else: # (cross)
        mazeFunctionFile.write("execute if score #maze spawntimer matches 5 run ")
        mazeFunctionFile.write("place template maze:cross ")
        mazeFunctionFile.write(str(x))
        mazeFunctionFile.write(" 0 ")
        mazeFunctionFile.write(str(z))
        mazeFunctionFile.write("\n")
    
    mazeFunctionFile.write("execute if score #maze spawntimer matches 20 run ")
    mazeFunctionFile.write("scoreboard players set #maze spawncomplete 1\n")

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

  print("Done")
  print("Copy the mazeworld folder from inside the maze folder to your Minecraft world saves, then enter the world to play.")
  print("You can also preview the maze by looking at maze.txt in the maze folder.")

if __name__ == "__main__": main()
