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
        mazeFunctionFile.write(" run place template maze:start ")
        mazeFunctionFile.write(str(x))
        mazeFunctionFile.write(" 0 ")
        mazeFunctionFile.write(str(z))
        mazeFunctionFile.write("\n")
        tick = tick + 1
        mazeFunctionFile.write("execute if score #maze spawntimer matches ")
        mazeFunctionFile.write(str(tick))
        mazeFunctionFile.write(" run forceload remove ")
        mazeFunctionFile.write(str(x))
        mazeFunctionFile.write(" ")
        mazeFunctionFile.write(str(z))
        mazeFunctionFile.write("\n")
      elif type == "end":
        if   room.getOpening("+x") == True:
          x = x + 15
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
          mazeFunctionFile.write(" run place template maze:end1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" clockwise_90\n")
          tick = tick + 1
          mazeFunctionFile.write("execute if score #maze spawntimer matches ")
          mazeFunctionFile.write(str(tick))
          mazeFunctionFile.write(" run forceload remove ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
        elif room.getOpening("-x") == True:
          z = z + 15
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
          mazeFunctionFile.write(" run place template maze:end1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" counterclockwise_90\n")
          tick = tick + 1
          mazeFunctionFile.write("execute if score #maze spawntimer matches ")
          mazeFunctionFile.write(str(tick))
          mazeFunctionFile.write(" run forceload remove ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
        elif room.getOpening("+z") == True:
          x = x + 15
          z = z + 15
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
          mazeFunctionFile.write(" run place template maze:end1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write(" 180\n")
          tick = tick + 1
          mazeFunctionFile.write("execute if score #maze spawntimer matches ")
          mazeFunctionFile.write(str(tick))
          mazeFunctionFile.write(" run forceload remove ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
        elif room.getOpening("-z") == True:
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
          mazeFunctionFile.write(" run place template maze:end1 ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
          tick = tick + 1
          mazeFunctionFile.write("execute if score #maze spawntimer matches ")
          mazeFunctionFile.write(str(tick))
          mazeFunctionFile.write(" run forceload remove ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" ")
          mazeFunctionFile.write(str(z))
          mazeFunctionFile.write("\n")
      else:
        numOpenings = 0
        for direction in directions:
          if room.openings[direction] == True: numOpenings = numOpenings + 1
        if   numOpenings == 1: # deadend
          if   room.getOpening("+x") == True:
            x = x + 15
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
            if   type == "normal": mazeFunctionFile.write("deadend1 ")
            elif type == "chest":  mazeFunctionFile.write("deadend1c ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" 0 ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write(" clockwise_90\n")
            tick = tick + 1
            mazeFunctionFile.write("execute if score #maze spawntimer matches ")
            mazeFunctionFile.write(str(tick))
            mazeFunctionFile.write(" run forceload remove ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
          elif room.getOpening("-x") == True:
            z = z + 15
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
            if   type == "normal": mazeFunctionFile.write("deadend1 ")
            elif type == "chest":  mazeFunctionFile.write("deadend1c ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" 0 ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write(" counterclockwise_90\n")
            tick = tick + 1
            mazeFunctionFile.write("execute if score #maze spawntimer matches ")
            mazeFunctionFile.write(str(tick))
            mazeFunctionFile.write(" run forceload remove ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
          elif room.getOpening("+z") == True:
            x = x + 15
            z = z + 15
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
            if   type == "normal": mazeFunctionFile.write("deadend1 ")
            elif type == "chest":  mazeFunctionFile.write("deadend1c ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" 0 ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write(" 180\n")
            tick = tick + 1
            mazeFunctionFile.write("execute if score #maze spawntimer matches ")
            mazeFunctionFile.write(str(tick))
            mazeFunctionFile.write(" run forceload remove ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
          elif room.getOpening("-z") == True:
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
            if   type == "normal": mazeFunctionFile.write("deadend1 ")
            elif type == "chest":  mazeFunctionFile.write("deadend1c ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" 0 ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
            tick = tick + 1
            mazeFunctionFile.write("execute if score #maze spawntimer matches ")
            mazeFunctionFile.write(str(tick))
            mazeFunctionFile.write(" run forceload remove ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
        elif numOpenings == 2: # hall or turn
          if room.getOpening("+x") == room.getOpening("-x"): # hall
            if room.getOpening("+x") == True:
              z = z + 15
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
              if type == "normal":  mazeFunctionFile.write("hall5 ")
              elif type == "chest": mazeFunctionFile.write("hall5c ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" 0 ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write(" counterclockwise_90")
              mazeFunctionFile.write("\n")
              tick = tick + 1
              mazeFunctionFile.write("execute if score #maze spawntimer matches ")
              mazeFunctionFile.write(str(tick))
              mazeFunctionFile.write(" run forceload remove ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write("\n")
            else:
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
              if type == "normal":  mazeFunctionFile.write("hall5 ")
              elif type == "chest": mazeFunctionFile.write("hall5c ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" 0 ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write("\n")
              tick = tick + 1
              mazeFunctionFile.write("execute if score #maze spawntimer matches ")
              mazeFunctionFile.write(str(tick))
              mazeFunctionFile.write(" run forceload remove ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write("\n")
          else: # turn
            if   (room.getOpening("+x") == True) and (room.getOpening("+z") == True):
              x = x + 15
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
              if   type == "normal": mazeFunctionFile.write("turn3 ")
              elif type == "chest":  mazeFunctionFile.write("turn3c ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" 0 ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write(" clockwise_90\n")
              tick = tick + 1
              mazeFunctionFile.write("execute if score #maze spawntimer matches ")
              mazeFunctionFile.write(str(tick))
              mazeFunctionFile.write(" run forceload remove ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write("\n")
            elif (room.getOpening("-x") == True) and (room.getOpening("+z") == True):
              x = x + 15
              z = z + 15
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
              if   type == "normal": mazeFunctionFile.write("turn3 ")
              elif type == "chest":  mazeFunctionFile.write("turn3c ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" 0 ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write(" 180\n")
              tick = tick + 1
              mazeFunctionFile.write("execute if score #maze spawntimer matches ")
              mazeFunctionFile.write(str(tick))
              mazeFunctionFile.write(" run forceload remove ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write("\n")
            elif (room.getOpening("-x") == True) and (room.getOpening("-z") == True):
              z = z + 15
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
              if   type == "normal": mazeFunctionFile.write("turn3 ")
              elif type == "chest":  mazeFunctionFile.write("turn3c ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" 0 ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write(" counterclockwise_90\n")
              tick = tick + 1
              mazeFunctionFile.write("execute if score #maze spawntimer matches ")
              mazeFunctionFile.write(str(tick))
              mazeFunctionFile.write(" run forceload remove ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write("\n")
            elif (room.getOpening("+x") == True) and (room.getOpening("-z") == True):
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
              if   type == "normal": mazeFunctionFile.write("turn3 ")
              elif type == "chest":  mazeFunctionFile.write("turn3c ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" 0 ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write("\n")
              tick = tick + 1
              mazeFunctionFile.write("execute if score #maze spawntimer matches ")
              mazeFunctionFile.write(str(tick))
              mazeFunctionFile.write(" run forceload remove ")
              mazeFunctionFile.write(str(x))
              mazeFunctionFile.write(" ")
              mazeFunctionFile.write(str(z))
              mazeFunctionFile.write("\n")
        elif numOpenings == 3: # tee
          if   room.getOpening("+x") == False:
            x = x + 15
            z = z + 15
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
            if type == "normal":  mazeFunctionFile.write("tee7 ")
            elif type == "chest": mazeFunctionFile.write("tee7c ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" 0 ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write(" 180\n")
            tick = tick + 1
            mazeFunctionFile.write("execute if score #maze spawntimer matches ")
            mazeFunctionFile.write(str(tick))
            mazeFunctionFile.write(" run forceload remove ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
          elif room.getOpening("-x") == False:
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
            if type == "normal":  mazeFunctionFile.write("tee7 ")
            elif type == "chest": mazeFunctionFile.write("tee7c ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" 0 ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
            tick = tick + 1
            mazeFunctionFile.write("execute if score #maze spawntimer matches ")
            mazeFunctionFile.write(str(tick))
            mazeFunctionFile.write(" run forceload remove ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
          elif room.getOpening("+z") == False:
            z = z + 15
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
            if type == "normal":  mazeFunctionFile.write("tee7 ")
            elif type == "chest": mazeFunctionFile.write("tee7c ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" 0 ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write(" counterclockwise_90\n")
            tick = tick + 1
            mazeFunctionFile.write("execute if score #maze spawntimer matches ")
            mazeFunctionFile.write(str(tick))
            mazeFunctionFile.write(" run forceload remove ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
          elif room.getOpening("-z") == False:
            x = x + 15
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
            if type == "normal":  mazeFunctionFile.write("tee7 ")
            elif type == "chest": mazeFunctionFile.write("tee7c ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" 0 ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write(" clockwise_90\n")
            tick = tick + 1
            mazeFunctionFile.write("execute if score #maze spawntimer matches ")
            mazeFunctionFile.write(str(tick))
            mazeFunctionFile.write(" run forceload remove ")
            mazeFunctionFile.write(str(x))
            mazeFunctionFile.write(" ")
            mazeFunctionFile.write(str(z))
            mazeFunctionFile.write("\n")
        elif numOpenings == 4: # cross
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
          if   type == "normal": mazeFunctionFile.write("cross ")
          elif type == "chest":  mazeFunctionFile.write("crossc ")
          mazeFunctionFile.write(str(x))
          mazeFunctionFile.write(" 0 ")
          mazeFunctionFile.write(str(z))
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
      mazesize_str = input("Maze size: ")
    else: break

  print("Generating maze...")
  maze = generateMaze(mazesize)

  sendMazeToMinecraft(maze)

  print("Done")
  print("Copy the mazeworld folder to your server folder.")

if __name__ == "__main__": main()
