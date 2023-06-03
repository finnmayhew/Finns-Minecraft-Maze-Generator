scoreboard players add #maze starttimer 1

execute if score #maze starttimer matches 1 run team modify players nametagVisibility hideForOwnTeam
execute if score #maze starttimer matches 1 run tellraw @a "One minute until friendly fire is enabled"
execute if score #maze starttimer matches 1200 run team modify players friendlyFire true
execute if score #maze starttimer matches 1200 run tellraw @a "Friendly fire is enabled"

execute if score #maze starttimer matches 1200 run scoreboard players set #maze gamephase 3
