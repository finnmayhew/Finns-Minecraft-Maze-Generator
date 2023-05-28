import copy
import random

# Config

air  = '☐'
wall = ' '


# Reference

directions = {'n', 'e', 's', 'w'}


# Classes

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({self.x}, {self.y})"
    
  def move(self, direction):
    if   direction == 'n': self.x = self.x - 1
    elif direction == 'e': self.y = self.y + 1
    elif direction == 's': self.x = self.x + 1
    elif direction == 'w': self.y = self.y - 1
    else:                  raise Exception("Direction must be in {n, e, s, w}")

class Maze:
  def __init__(self, width, height):
    self.width  = width
    self.height = height
    self.maze   = [[wall for i in range(width)] for j in range(height)]
  
  def draw(self):
    for row in self.maze:
      print(*row)

  def getValue(self, point):
    if (point.x == -1) or (point.y == -1): return None
    try:    value = self.maze[point.x][point.y]
    except: return None
    else:   return value
  
  def setValue(self, point, value):
    if (point.x == -1) or (point.y == -1): print("Cannot set value at", point, "(outside of maze)")
    try:    self.maze[point.x][point.y] = value
    except: print("Cannot set value at", point, "(outside of maze)")


# Functions

def generateRectangularMaze(width, height):
  print("Generating maze...")

  maze = Maze(width,height)

  pastPathPoints = set()

  head = Point(0,0)
  maze.setValue(head, air)
  pastPathPoints.add(head)

  while True:
    possibleNextHeads = set()
    for direction in directions:
      look = copy.deepcopy(head)
      look.move(direction)
      if maze.getValue(look) == wall:
        possibleNextHeads.add(look)
    
    viableNextHeads = set()
    for possibleNextHead in possibleNextHeads:
      numPathNear = 0
      for direction in directions:
        look2 = copy.deepcopy(possibleNextHead)
        look2.move(direction)
        if maze.getValue(look2) == air: numPathNear = numPathNear + 1
      if numPathNear == 1: viableNextHeads.add(possibleNextHead)
    
    if len(viableNextHeads) == 0:
      head = random.choice(list(pastPathPoints))
      continue

    head = random.choice(list(viableNextHeads))
    maze.setValue(head, air)
    pastPathPoints.add(head)

    if (head.x == maze.height - 1) and (head.y == maze.width - 1): break

  maze.draw()

def main():
  print("-- Welcome to Finn's Minecraft Maze Generator --")
  print("------------------------------------------------")
  while True:
    print("What type of maze should we generate?")
    mazetype = input("Options: square (s), rectangle (r): ")
    if (mazetype == "s"):
      width_str = input("Sidelength: ")
      while True:
        try:
          width = abs(int(width_str))
          height = width
          break
        except:
          print("Sidelength must be an integer value")
          width_str = input("Sidelength: ")
      break
    elif (mazetype == "r"):
      width_str  = input("Width: ")
      while True:
        try:
          width = abs(int(width_str))
          break
        except:
          print("Width must be an integer value")
          width_str = input("Width: ")
      height_str = input("Height: ")
      while True:
        try:
          height = abs(int(height_str))
          break
        except:
          print("Height must be an integer value")
          height_str = input("Height: ")
      break
    else:
      print("Must put either 's' or 'r'")
  
  generateRectangularMaze(width=width, height=height)

if __name__ == "__main__":
  main()
