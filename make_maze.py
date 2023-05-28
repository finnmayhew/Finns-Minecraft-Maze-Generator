import copy
import random

# Config

air  = '█'
wall = ' '
edge = '░'

density = 0.2 # any positive number


# Reference

directions = {'n', 'e', 's', 'w'}


# Classes

class Point:
  def __init__(self, x, y):
    if (x < 0) or (y < 0):
      raise Exception("Points must have non-negative coordinates")
    self.x = x
    self.y = y

  def __eq__(self, other):
    if isinstance(other, self.__class__): return (self.x == other.x) and (self.y == other.y)
    return False
  
  def __hash__(self):
    return hash((self.x, self.y))

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
    self.start  = Point(1, 1)
    self.end    = Point(height - 2, width - 2)
    
    self.maze[0] = [edge for i in range(width)]
    self.maze[height - 1] = [edge for i in range(width)]
    for j in range(height):
      for i in range(width):
        if (i == 0) or (i == width - 1): self.maze[j][i] = edge

  def draw(self):
    with open("maze/maze.txt", 'w') as mazeImageFile:
      for row in self.maze:
        for entry in row:
          mazeImageFile.writelines(entry)
        mazeImageFile.write('\n')

  def getValue(self, point):
    try:    value = self.maze[point.x][point.y]
    except: return None
    else:   return value

  def setValue(self, point, value):
    try:    self.maze[point.x][point.y] = value
    except: print("Cannot set value at", point, "(outside of maze)")


# Functions

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
  print("------------------------------------------------")
  print("-- Welcome to Finn's Minecraft Maze Generator --")
  print("------------------------------------------------")
  while True:
    print("What type of maze should we generate?")
    mazetype = input("Options: square (s), rectangle (r): ")
    if (mazetype == "s"):
      width_str = input("Sidelength: ")
      while True:
        try:
          width  = abs(int(width_str))
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
  
  print("Generating maze...")
  while True:
    maze, foundEnd = generateRectangularMaze(width=width, height=height)
    if foundEnd: break
  
  maze.draw()

if __name__ == "__main__":
  main()
