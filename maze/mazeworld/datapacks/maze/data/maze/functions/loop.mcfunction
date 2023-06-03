execute if score #maze gamephase matches 0 run function maze:make_maze
execute if score #maze gamephase matches 1 run function maze:waiting_to_drop
execute if score #maze gamephase matches 2 run function maze:game_start
