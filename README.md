# Finn's Minecraft Maze Generator

When this is at a working state, run

```bash
python make_maze.py
```

to generate a maze. Configuration and further instruction will appear in the shell.

The workflow of the code will be:

- `make_maze.py` generates the maze and outputs it to `maze.png` and `maze.zip`
- The user places `maze.zip` into a world datapack folder, then the datapack's code is run when the world is opened
