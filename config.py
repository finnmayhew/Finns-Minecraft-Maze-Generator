'''
Non-command-line config options

Contains:
- tile characters for maze text file
- maze density multiplier
- list of possible directions within the maze
'''

air  = '█'
wall = ' '
edge = '░'

density = 0.2 # any positive number

directions = {'n', 'e', 's', 'w'}
roomVariants = {
    "normal": 15,
    "chest":  1
}
