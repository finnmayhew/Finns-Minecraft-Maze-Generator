execute as @a run scoreboard players add #maze numplayers 1

give @a tripwire_hook{display:{Name:'[{"text":"Key","italic":false}]'}}
scoreboard objectives setdisplay sidebar numkeys

scoreboard players set @a readytogetitems 1

team modify players nametagVisibility hideForOwnTeam

tellraw @a "One minute until PvP is enabled"
schedule function maze:enablepvp 60s

scoreboard players set #maze gamephase 3
