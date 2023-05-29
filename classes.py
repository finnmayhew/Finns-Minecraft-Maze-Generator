'''
Class definitions

Contains:
- Point
- Maze
'''

import json

from config import *

class Point:
  '''
  variables:
  - x
  - y
  
  methods:
  - move(direction)
  '''

  def __init__(self, x, y):
    if (x < 0) or (y < 0): raise Exception("Points must have non-negative coordinates")
    self.x = x
    self.y = y

  def __eq__(self, other):
    if isinstance(other, self.__class__): return (self.x == other.x) and (self.y == other.y)
    return False

  def __hash__(self): return hash((self.x, self.y))

  def __str__(self): return f"({self.x}, {self.y})"

  def move(self, direction):
    if   direction == 'n': self.x = self.x - 1
    elif direction == 'e': self.y = self.y + 1
    elif direction == 's': self.x = self.x + 1
    elif direction == 'w': self.y = self.y - 1
    else:                  raise Exception("Direction must be in {n, e, s, w}")

class Maze:
  '''
  variables:
  - width
  - height
  - maze ([i/x/row][j/y/column])
  - start
  - end
  - encodedMaze
  
  methods:
  - getValue(point)
  - setValue(point)
  - draw()
  - encode()
  '''
  def __init__(self, width, height):
    self.width       = width
    self.height      = height
    self.maze        = [[wall for j in range(width)] for i in range(height)]
    self.start       = Point(1, 1)
    self.end         = Point(height - 2, width - 2)
    self.encodedMaze = dict()

    self.maze[0] = [edge for j in range(width)]
    self.maze[height - 1] = [edge for j in range(width)]
    for i in range(height):
      for j in range(width):
        if (j == 0) or (j == width - 1): self.maze[i][j] = edge

  def getValue(self, point):
    try:    value = self.maze[point.x][point.y]
    except: return None
    else:   return value

  def setValue(self, point, value):
    try:    self.maze[point.x][point.y] = value
    except: print("Cannot set value at", point, "(outside of maze)")

  def draw(self):
    with open("maze/maze.txt", 'w') as mazeImageFile:
      for row in self.maze:
        for entry in row:
          mazeImageFile.writelines(entry)
        mazeImageFile.write('\n')

  def encode(self):
    self.encodedMaze = {
      "rooms": []
    }
    for i in range(self.height):
      for j in range(self.width):
        if   (i == self.start.x) and (j == self.start.y):
          if   self.maze[i+1][j] == wall:                                    self.encodedMaze["rooms"].append(dict(x=i, y=j, type="start",   orientation=2))
          elif self.maze[i][j+1] == wall:                                    self.encodedMaze["rooms"].append(dict(x=i, y=j, type="start",   orientation=4))
          else:                                                              self.encodedMaze["rooms"].append(dict(x=i, y=j, type="start",   orientation=6))
        elif (i == self.end.x)   and (j == self.end.y):
          if self.maze[i-1][j] == air:                                       self.encodedMaze["rooms"].append(dict(x=i, y=j, type="end",     orientation=1))
          else:                                                              self.encodedMaze["rooms"].append(dict(x=i, y=j, type="end",     orientation=8))
        elif self.maze[i][j] == edge:                                        self.encodedMaze["rooms"].append(dict(x=i, y=j, type="edge",    orientation=0))
        elif self.maze[i][j] == wall:                                        self.encodedMaze["rooms"].append(dict(x=i, y=j, type="wall",    orientation=0))
        elif self.maze[i][j] == air:
          nearbyAir = 0
          for direction in directions:
            look = Point(i, j)
            look.move(direction)
            if self.maze[look.x][look.y] == air: nearbyAir = nearbyAir + 1
          if   nearbyAir == 1:
            if   self.maze[i-1][j] == air:                                   self.encodedMaze["rooms"].append(dict(x=i, y=j, type="deadend", orientation=1))
            elif self.maze[i][j+1] == air:                                   self.encodedMaze["rooms"].append(dict(x=i, y=j, type="deadend", orientation=2))
            elif self.maze[i+1][j] == air:                                   self.encodedMaze["rooms"].append(dict(x=i, y=j, type="deadend", orientation=4))
            else:                                                            self.encodedMaze["rooms"].append(dict(x=i, y=j, type="deadend", orientation=8))
          elif nearbyAir == 2:
            if   (self.maze[i-1][j] == air) and (self.maze[i][j+1] == air):  self.encodedMaze["rooms"].append(dict(x=i, y=j, type="turn",    orientation=3))
            elif (self.maze[i+1][j] == air) and (self.maze[i][j+1] == air):  self.encodedMaze["rooms"].append(dict(x=i, y=j, type="turn",    orientation=6))
            elif (self.maze[i-1][j] == air) and (self.maze[i][j-1] == air):  self.encodedMaze["rooms"].append(dict(x=i, y=j, type="turn",    orientation=9))
            elif (self.maze[i+1][j] == air) and (self.maze[i][j-1] == air):  self.encodedMaze["rooms"].append(dict(x=i, y=j, type="turn",    orientation=12))
            elif (self.maze[i-1][j] == air) and (self.maze[i+1][j] == air):  self.encodedMaze["rooms"].append(dict(x=i, y=j, type="hall",    orientation=5))
            else:                                                            self.encodedMaze["rooms"].append(dict(x=i, y=j, type="hall",    orientation=10))
          elif nearbyAir == 3:
            if   (self.maze[i][j-1] == wall) or (self.maze[i][j-1] == edge): self.encodedMaze["rooms"].append(dict(x=i, y=j, type="tee",     orientation=7))
            elif (self.maze[i+1][j] == wall) or (self.maze[i+1][j] == edge): self.encodedMaze["rooms"].append(dict(x=i, y=j, type="tee",     orientation=11))
            elif (self.maze[i][j+1] == wall) or (self.maze[i][j+1] == edge): self.encodedMaze["rooms"].append(dict(x=i, y=j, type="tee",     orientation=13))
            else:                                                            self.encodedMaze["rooms"].append(dict(x=i, y=j, type="tee",     orientation=14))
          else:                                                              self.encodedMaze["rooms"].append(dict(x=i, y=j, type="cross",   orientation=15))
    with open("maze/maze.json", 'w') as mazeJsonFile: json.dump(self.encodedMaze,mazeJsonFile)
