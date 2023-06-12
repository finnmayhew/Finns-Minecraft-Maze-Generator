execute as @a store result score @s numkeys run clear @s tripwire_hook 0

execute as @e[type=item,nbt={Item:{tag:{noDespawn:1b}}}] run data merge entity @s {Age:-32768}

effect give @a saturation infinite 0 true


execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s wooden_sword 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s shield 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s splash_potion{display:{Name:'{"text":"10s of Speed"}'},CustomPotionEffects:[{Id:1,Duration:200}],CustomPotionColor:8303306} 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s splash_potion{display:{Name:'{"text":"10s of Strength"}'},CustomPotionEffects:[{Id:5,Duration:200}],CustomPotionColor:9839908} 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s splash_potion{display:{Name:'{"text":"10s of Jump"}'},CustomPotionEffects:[{Id:8,Duration:200}],CustomPotionColor:2358349} 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s splash_potion{display:{Name:'{"text":"10s of Invisibility"}'},CustomPotionEffects:[{Id:14,Duration:200}],CustomPotionColor:8488341} 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run scoreboard players set @s readytogetitems 0

execute as @p[x=7,y=91,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=0}] run scoreboard players set @s readytogetitems 1

execute as @e[type=item,nbt={Item:{id:"minecraft:tripwire_hook"}}] run data merge entity @s {Age:1}

execute as @a at @s if score @s numkeys = #maze numplayers if block ~ ~-1 ~ glowstone run scoreboard players set @s winner 1
execute as @p[scores={winner=1}] run scoreboard players set #maze gamephase 4
