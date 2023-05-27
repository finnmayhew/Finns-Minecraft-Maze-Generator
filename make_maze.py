import random

def makeSolutionPath(maze):

  # Start at top left corner
  head = [0,0]
  maze[head[0]][head[1]] = 1

  # Walk until it gets to the end
  step = 0
  while True:

    # Take one step
    while True:
      direction = random.randint(1,4)

      tentativeHeadFound = False
      if direction == 1:
        if head[0] != 0:
          tentativeHead = [head[0] - 1, head[1]]
          tentativeHeadFound = True
      if direction == 2:
        if head[1] != len(maze[0]) - 1:
          tentativeHead = [head[0], head[1] + 1]
          tentativeHeadFound = True
      if direction == 3:
        if head[1] != len(maze) - 1:
          tentativeHead = [head[0] + 1, head[1]]
          tentativeHeadFound = True
      if direction == 4:
        if head[1] != 0:
          tentativeHead = [head[0], head[1] - 1]
          tentativeHeadFound = True
      
      if tentativeHeadFound:
        if direction == 1:
          if tentativeHead[0] != 0:
            if (maze[tentativeHead[0] - 1][tentativeHead[1]] == 0) and (maze[tentativeHead[0]][tentativeHead[1] + 1] == 0) and (maze[tentativeHead[0]][tentativeHead[1] - 1] == 0):
              head = tentativeHead
              break
          else:
            if (maze[tentativeHead[0]][tentativeHead[1] + 1] == 0) and (maze[tentativeHead[0]][tentativeHead[1] - 1] == 0):
              head = tentativeHead
              break
        if direction == 2:
          if tentativeHead[1] != len(maze[0]) - 1:
            if (maze[tentativeHead[0] - 1][tentativeHead[1]] == 0) and (maze[tentativeHead[0]][tentativeHead[1] + 1] == 0) and (maze[tentativeHead[0] + 1][tentativeHead[1]] == 0):
              head = tentativeHead
              break
          else:
            if (maze[tentativeHead[0] - 1][tentativeHead[1]] == 0) and (maze[tentativeHead[0] + 1][tentativeHead[1]] == 0):
              head = tentativeHead
              break
        if direction == 3:
          if tentativeHead[1] != len(maze) - 1:
            if (maze[tentativeHead[0]][tentativeHead[1] + 1] == 0) and (maze[tentativeHead[0] + 1][tentativeHead[1]] == 0) and (maze[tentativeHead[0]][tentativeHead[1] - 1] == 0):
              head = tentativeHead
              break
          else:
            if (maze[tentativeHead[0]][tentativeHead[1] + 1] == 0) and (maze[tentativeHead[0]][tentativeHead[1] - 1] == 0):
              head = tentativeHead
              break
        if direction == 4:
          if tentativeHead[1] != 0:
            if (maze[tentativeHead[0] - 1][tentativeHead[1]] == 0) and (maze[tentativeHead[0] + 1][tentativeHead[1]] == 0) and (maze[tentativeHead[0]][tentativeHead[1] - 1] == 0):
              head = tentativeHead
              break
          else:
            if (maze[tentativeHead[0] - 1][tentativeHead[1]] == 0) and (maze[tentativeHead[0] + 1][tentativeHead[1]] == 0):
              head = tentativeHead
              break
    
    maze[head[0]][head[1]] = 1
    step = step + 1

    # print("took step",step)

    if (head == [len(maze) - 1, len(maze[0]) - 1]) or (step == 50):
      break


def generateRectangularMaze(width, height):
  print("Generating maze...")

  maze = [[0 for i in range(width)] for j in range(height)]

  makeSolutionPath(maze)

  for row in maze:
    print(*row)

def main():
  print("-- Welcome to Finn's Minecraft Maze Generator --")
  print("------------------------------------------------")
  mazename = input("Name the maze: ")
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
  if (mazetype == "r"):
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
  
  generateRectangularMaze(width=width, height=height)

if __name__ == "__main__":
  main()
