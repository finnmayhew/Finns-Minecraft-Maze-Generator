scoreboard players add #maze starttimer 1

execute if score #maze starttimer matches 1 run execute as @a run scoreboard players add #maze numplayers 1

execute if score #maze starttimer matches 1 run give @a tripwire_hook{display:{Name:'[{"text":"Key","italic":false}]'},noDespawn:1b} 1
execute if score #maze starttimer matches 2 run scoreboard objectives setdisplay sidebar numkeys

execute if score #maze starttimer matches 1 run team modify players nametagVisibility hideForOwnTeam
execute if score #maze starttimer matches 1 run tellraw @a "One minute until PvP is enabled"

execute if score #maze starttimer matches 1200 run team modify players friendlyFire true
execute if score #maze starttimer matches 1200 run tellraw @a "PvP is enabled"

execute if score #maze starttimer matches 1200 run scoreboard players set #maze gamephase 3
