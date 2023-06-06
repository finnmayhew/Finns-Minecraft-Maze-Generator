execute as @a store result score @s numkeys run clear @s tripwire_hook 0

execute as @e[type=item,nbt={Item:{tag:{noDespawn:1b}}}] run data merge entity @s {Age:-32768}

effect give @a saturation infinite 0 true

execute as @a at @s if score @s numkeys = #maze numplayers if block ~ ~-1 ~ glowstone run scoreboard players set @s winner 1
execute as @p[scores={winner=1}] run scoreboard players set #maze gamephase 4
