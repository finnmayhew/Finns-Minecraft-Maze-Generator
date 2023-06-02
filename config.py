'''
Non-command-line config options

Contains:
- tile characters for maze text file
- maze density multiplier
- room variant weights
- list of possible directions within the maze
'''

air  = '█'
wall = ' '
edge = '░'

density = 0.2 # any positive number
roomVariants = {
    "normal": 17,
    "chest":  1
}

directions = {'n', 'e', 's', 'w'}
