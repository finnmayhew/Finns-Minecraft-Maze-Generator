'''
Maze generation script

Arguments are passed through command-line prompts

For other configuration, see `config.py`
'''

import random
from math import ceil

from classes import *
from config import *

def sendMazeToMinecraft(maze):
  with open("mazeworld/datapacks/maze/data/maze/functions/make_maze.mcfunction", 'w') as mazeFunctionFile:
    mazeFunctionFile.write("scoreboard players add #maze spawntimer 1\n")
    mazeFunctionFile.write("gamemode adventure @a\n")
    mazeFunctionFile.write("spawnpoint @a 7 100 -4\n")
    
    tick = 1
    for room in maze.getRooms():
      x = room.position["xChunk"]*16
      z = room.position["zChunk"]*16
      type = room.getType()

      if   type == "start":
        template = "start"
        rotation = None
      elif type == "end":
        template = "end1"
        if   room.getOpening("+x") == True: rotation = "clockwise_90"
        elif room.getOpening("-x") == True: rotation = "counterclockwise_90"
        elif room.getOpening("+z") == True: rotation = "180" # x and z + 15
        elif room.getOpening("-z") == True: rotation = None
      else:
        numOpenings = 0
        for direction in directions:
          if room.openings[direction] == True: numOpenings = numOpenings + 1
        if   numOpenings == 1:
          template = "deadend1"
          if   room.getOpening("+x") == True: rotation = "clockwise_90"
          elif room.getOpening("-x") == True: rotation = "counterclockwise_90"
          elif room.getOpening("+z") == True: rotation = "180"
          elif room.getOpening("-z") == True: rotation = None
        elif numOpenings == 2:
          if room.getOpening("+x") == room.getOpening("-x"):
            template = "hall5"
            if room.getOpening("+x") == True: rotation = "counterclockwise_90"
            else:                             rotation = None
          else:
            template = "turn3"
            if   (room.getOpening("+x") == True) and (room.getOpening("+z") == True): rotation = "clockwise_90"
            elif (room.getOpening("-x") == True) and (room.getOpening("+z") == True): rotation = "180"
            elif (room.getOpening("-x") == True) and (room.getOpening("-z") == True): rotation = "counterclockwise_90"
            elif (room.getOpening("+x") == True) and (room.getOpening("-z") == True): rotation = None
        elif numOpenings == 3:
          template = "tee7"
          if   room.getOpening("+x") == False: rotation = "180"
          elif room.getOpening("-x") == False: rotation = None
          elif room.getOpening("+z") == False: rotation = "counterclockwise_90"
          elif room.getOpening("-z") == False: rotation = "clockwise_90"
        elif numOpenings == 4:
          template = "cross"

      if (rotation == "clockwise_90")        or (rotation == "180"): x = x + 15
      if (rotation == "counterclockwise_90") or (rotation == "180"): z = z + 15

      mazeFunctionFile.write("execute if score #maze spawntimer matches ")
      mazeFunctionFile.write(str(tick))
      mazeFunctionFile.write(" run forceload add ")
      mazeFunctionFile.write(str(x))
      mazeFunctionFile.write(" ")
      mazeFunctionFile.write(str(z))
      mazeFunctionFile.write("\n")
      tick = tick + 1
      mazeFunctionFile.write("execute if score #maze spawntimer matches ")
      mazeFunctionFile.write(str(tick))
      mazeFunctionFile.write(" run place template maze:")
      mazeFunctionFile.write(template)
      if type == "chest":
        mazeFunctionFile.write("c")
      mazeFunctionFile.write(" ")
      mazeFunctionFile.write(str(x))
      mazeFunctionFile.write(" 0 ")
      mazeFunctionFile.write(str(z))
      if rotation is not None:
        mazeFunctionFile.write(" ")
        mazeFunctionFile.write(rotation)
      mazeFunctionFile.write("\n")
      tick = tick + 1
      mazeFunctionFile.write("execute if score #maze spawntimer matches ")
      mazeFunctionFile.write(str(tick))
      mazeFunctionFile.write(" run forceload remove ")
      mazeFunctionFile.write(str(x))
      mazeFunctionFile.write(" ")
      mazeFunctionFile.write(str(z))
      mazeFunctionFile.write("\n")

      tick = tick + 1

    mazeFunctionFile.write("execute if score #maze spawntimer matches ")
    mazeFunctionFile.write(str(tick))
    mazeFunctionFile.write(" run kill @e[name=\"Loading...\"]\n")
    mazeFunctionFile.write("execute if score #maze spawntimer matches ")
    mazeFunctionFile.write(str(tick))
    mazeFunctionFile.write(" run summon minecraft:armor_stand 8.0 101.25 4.0 {CustomName:'[{\"text\":\"Enter the maze\",\"color\":\"green\"}]',CustomNameVisible:1,Invisible:1,Marker:1,NoGravity:1}\n")
    mazeFunctionFile.write("execute if score #maze spawntimer matches ")
    mazeFunctionFile.write(str(tick))
    mazeFunctionFile.write(" run fill 7 100 4 8 100 4 air\n")
    mazeFunctionFile.write("execute if score #maze spawntimer matches ")
    mazeFunctionFile.write(str(tick))
    mazeFunctionFile.write(" run tellraw @a \"Maze loaded, enter when all players have joined\"\n")
    mazeFunctionFile.write("execute if score #maze spawntimer matches ")
    mazeFunctionFile.write(str(tick))
    mazeFunctionFile.write(" run scoreboard players set #maze gamephase 1\n")

def initializeMaze(maze):
  start = Room(0,0)

  start.setOpening("+x", True)
  start.setOpening("-x", True)
  start.setOpening("+z", True)
  start.setOpening("-z", True)
  
  start.setType("start")

  for direction in directions:
    maze.addOpenTile(start.position["xChunk"], start.position["zChunk"], offset=direction)

  maze.addRoom(start)

def generateMaze(mazesize):
  maze = Maze()
  initializeMaze(maze)

  numRooms = 1
  while (numRooms <= mazesize):
    openTile = maze.chooseRandomOpenTile()
    if openTile is None: # if the maze closes itself off before reaching the required size, make a new maze
      maze = Maze()
      initializeMaze(maze)
      numRooms = 1
      continue

    room = Room(openTile.position["xChunk"], openTile.position["zChunk"])

    for direction in directions:
      if maze.getRoom(room.position["xChunk"], room.position["zChunk"], offset=direction) is None:
        open = random.choices([True, False], wallWeights)[0]
        if open == True: maze.addOpenTile(room.position["xChunk"], room.position["zChunk"], offset=direction)
      else:
        if maze.getRoom(room.position["xChunk"], room.position["zChunk"], offset=direction).getOpening(direction, opposite=True) == True:
          open = True
        else:
          open = False
      room.setOpening(direction, open)

    room.setType(random.choices(["normal", "chest"], roomWeights)[0])

    maze.removeOpenTile(room.position["xChunk"], room.position["zChunk"])
    maze.addRoom(room)

    numRooms = numRooms + 1
  
  while True:
    openTile = maze.chooseRandomOpenTile()
    if openTile is None:
      break

    room = Room(openTile.position["xChunk"], openTile.position["zChunk"])

    for direction in directions:
      if maze.getRoom(room.position["xChunk"], room.position["zChunk"], offset=direction) is None:
        open = False
      else:
        if maze.getRoom(room.position["xChunk"], room.position["zChunk"], offset=direction).getOpening(direction, opposite=True) == True:
          open = True
        else:
          open = False
      room.setOpening(direction, open)
    
    room.setType(random.choices(["normal", "chest"], roomWeights)[0])

    maze.removeOpenTile(room.position["xChunk"], room.position["zChunk"])
    maze.addRoom(room)

  maze.setFinalRoomToEnd()

  return maze

def main():
  print(" -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
  print("| Welcome to Finn's Minecraft Maze Generator |")
  print(" -- -- -- -- -- -- -- -- -- -- -- -- -- -- --")
  while True:
    mazesize_str = input("Maze size: ")
    try: mazesize = abs(int(mazesize_str))
    except:
      print("Maze size must be an integer value")
    else: break

  print("Generating maze...")
  maze = generateMaze(mazesize)

  sendMazeToMinecraft(maze)

  print("Done")
  print("Copy the mazeworld folder to your server folder.")

if __name__ == "__main__": main()
