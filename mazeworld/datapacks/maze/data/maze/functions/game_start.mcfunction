scoreboard players add #maze starttimer 1

execute if score #maze starttimer matches 1 run execute as @a run scoreboard players add #maze numplayers 1

execute if score #maze starttimer matches 1 run give @a tripwire_hook{display:{Name:'[{"text":"Key","italic":false}]'},noDespawn:1b} 1
execute if score #maze starttimer matches 2 run scoreboard objectives setdisplay sidebar numkeys

execute if score #maze starttimer matches 1 run give @a golden_sword 1
execute if score #maze starttimer matches 1 run give @a shield 1
execute if score #maze starttimer matches 1 run give @a splash_potion{display:{Name:'{"text":"Speed"}'},CustomPotionEffects:[{Id:1,Duration:200}]} 2
execute if score #maze starttimer matches 1 run give @a splash_potion{display:{Name:'{"text":"Strength"}'},CustomPotionEffects:[{Id:5,Duration:200}]} 2
execute if score #maze starttimer matches 1 run give @a splash_potion{display:{Name:'{"text":"Jump"}'},CustomPotionEffects:[{Id:8,Duration:200}]} 2
execute if score #maze starttimer matches 1 run give @a splash_potion{display:{Name:'{"text":"Invisibility"}'},CustomPotionEffects:[{Id:14,Duration:200}]} 1

execute if score #maze starttimer matches 1 run team modify players nametagVisibility hideForOwnTeam
execute if score #maze starttimer matches 1 run tellraw @a "One minute until PvP is enabled"

execute if score #maze starttimer matches 1200 run team modify players friendlyFire true
execute if score #maze starttimer matches 1200 run tellraw @a "PvP is enabled"

execute if score #maze starttimer matches 1200 run scoreboard players set #maze gamephase 3
