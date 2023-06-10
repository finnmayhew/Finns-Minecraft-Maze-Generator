execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s wooden_sword 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s shield 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s splash_potion{display:{Name:'{"text":"Speed"}'},CustomPotionEffects:[{Id:1,Duration:200}]} 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s splash_potion{display:{Name:'{"text":"Strength"}'},CustomPotionEffects:[{Id:5,Duration:200}]} 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s splash_potion{display:{Name:'{"text":"Jump"}'},CustomPotionEffects:[{Id:8,Duration:200}]} 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run give @s splash_potion{display:{Name:'{"text":"Invisibility"}'},CustomPotionEffects:[{Id:14,Duration:200}]} 1
execute as @p[x=7,y=94,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=1}] run scoreboard players set @s readytogetitems 0

execute as @p[x=7,y=91,z=7,dx=1,dy=1,dz=1,scores={readytogetitems=0}] run scoreboard players set @s readytogetitems 1
