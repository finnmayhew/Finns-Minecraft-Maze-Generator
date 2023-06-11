# Finn's Minecraft PvP Maze Minigame

## How to use

Play in **Minecraft 1.20**.

Download this repository, then in a command prompt `cd` to your copy of the repository and run

```bash
python make_maze.py
```

The shell will prompt you to specify the maze size in rooms. Each room is one chunk (16 by 16 blocks). There are more config options in `config.py`.

Once the maze is generated, move the `mazeworld` folder to your server folder. When you start the server, the maze will generate. Wait in the lobby until everyone has joined.

## Gameplay

At the start of the game, every player is given a key item. In order to win, you have to get to the exit (marked by a 2 by 2 square of glowstone blocks) while holding all the keys. The sidebar shows how many keys each player has.

There are chests scattered throughout the maze guarded by small parkour challenges. Inside the chests are weapons and armor.

## Known issues

- Rarely a player will receive double items on drop
- Keys can despawn if left on the ground too long
