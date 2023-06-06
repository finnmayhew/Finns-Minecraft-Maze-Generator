'''
Class definitions

Contains:
- Room
- OpenTile
- Maze
'''

import random


directions = ["+x", "-x", "+z", "-z"]


class Room:
  '''
  variables:
  - position
  - openings
  - type

  methods:
  - setOpening(direction, value)
  - getOpening(direction)
  - setType(type)
  - getType()
  '''
  def __init__(self, xChunk, zChunk):
    self.position = {
      "xChunk": xChunk,
      "zChunk": zChunk
    }
    self.openings = {}
    for direction in directions: self.openings[direction] = None
    self.type = None
  
  def setOpening(self, direction, value):
    self.openings[direction] = value

  def getOpening(self, direction, opposite=False):
    if opposite == False:
      return self.openings[direction]
    else:
      if   direction == "+x": return self.openings["-x"]
      elif direction == "-x": return self.openings["+x"]
      elif direction == "+z": return self.openings["-z"]
      elif direction == "-z": return self.openings["+z"]

  def setType(self, type):
    self.type = type
  
  def getType(self):
    return self.type


class OpenTile:
  '''
  variables:
  - position
  '''

  def __init__(self, xChunk, zChunk):
    self.position = {
      "xChunk": xChunk,
      "zChunk": zChunk
    }


class Maze:
  '''
  variables:
  - rooms
  - openTiles

  methods:
  - addRoom(xChunk, zChunk)
  - getRoom(xChunk, zChunk, offset)
  - getRooms()
  - addOpenTile(xChunk, zChunk)
  - removeOpenTile(xChunk, zChunk)
  - chooseRandomOpenTile()
  - setFinalRoomToEnd()
  '''
  def __init__(self):
    self.rooms = []
    self.openTiles = set()

  def addRoom(self, room):
    self.rooms.append(room)

  def getRoom(self, xChunk, zChunk, offset=None):
    for room in self.rooms:
      if offset is None:
        if (room.position["xChunk"] == xChunk) and (room.position["zChunk"] == zChunk):
          return room
      elif offset == "+x":
        if (room.position["xChunk"] == xChunk + 1) and (room.position["zChunk"] == zChunk):
          return room
      elif offset == "-x":
        if (room.position["xChunk"] == xChunk - 1) and (room.position["zChunk"] == zChunk):
          return room
      elif offset == "+z":
        if (room.position["xChunk"] == xChunk) and (room.position["zChunk"] == zChunk + 1):
          return room
      elif offset == "-z":
        if (room.position["xChunk"] == xChunk) and (room.position["zChunk"] == zChunk - 1):
          return room
    return None

  def getRooms(self):
    return self.rooms

  def addOpenTile(self, xChunk, zChunk, offset=None):
    if offset == None:
      self.openTiles.add(OpenTile(xChunk, zChunk))
    elif offset == "+x":
      self.openTiles.add(OpenTile(xChunk + 1, zChunk))
    elif offset == "-x":
      self.openTiles.add(OpenTile(xChunk - 1, zChunk))
    elif offset == "+z":
      self.openTiles.add(OpenTile(xChunk, zChunk + 1))
    elif offset == "-z":
      self.openTiles.add(OpenTile(xChunk, zChunk - 1))

  def removeOpenTile(self, xChunk, zChunk):
    for openTile in list(self.openTiles):
      if (openTile.position["xChunk"] == xChunk) and (openTile.position["zChunk"] == zChunk):
        self.openTiles.remove(openTile)

  def chooseRandomOpenTile(self):
    if len(list(self.openTiles)) > 0:
      return random.choice(list(self.openTiles))
    else:
      return None

  def setFinalRoomToEnd(self):
    for room in self.rooms:
      numOpenings = 0
      for direction in directions:
        if room.openings[direction] == True: numOpenings = numOpenings + 1
      
      if numOpenings == 1:
        lastDeadEnd = room

    lastDeadEnd.setType("end")
