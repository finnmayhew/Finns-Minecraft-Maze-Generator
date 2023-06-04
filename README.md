# Finn's Minecraft PvP Maze Minigame

## How to use

Play on **Minecraft 1.19.4**.

Download this repository, then in a command prompt `cd` to your copy of the repository and run

```bash
python make_maze.py
```

The shell will prompt you to specify the maze size in rooms. Each room is one chunk (16 by 16 blocks).

Once the maze is generated, move the folder `maze/mazeworld` to your server folder. When you start the server, the maze will generate. Wait in the lobby until everyone has joined.

## Gameplay

At the start of the game, every player is given a key item. In order to win, you have to get to the exit (marked by a 2 by 2 square of glowstone blocks) while holding all the keys. The sidebar shows how many keys each player has.

There are chests scattered throughout the maze guarded by small parkour challenges. Inside the chests are weapons and armor.

## More info

You can preview a maze outside of Minecraft at `maze/maze.txt`.

In `config.py`, you can configure

- What text characters are used in `maze/maze.txt`
- How dense the maze is
- The frequency chest rooms will appear

## To do

- Playtest
- Add more room types
- Upgrade the visuals
- Add more maze generation algorithms
