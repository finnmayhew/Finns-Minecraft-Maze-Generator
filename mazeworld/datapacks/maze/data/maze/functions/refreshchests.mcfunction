execute as @e[tag=normalchest] at @s run data modify block ~ ~ ~ LootTable set value "maze:normalchest"

schedule function maze:refreshchests 180s
