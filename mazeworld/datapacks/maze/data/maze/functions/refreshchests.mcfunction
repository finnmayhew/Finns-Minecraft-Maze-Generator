execute as @e[tag=normalchest] at @s run setblock ~ ~ ~ air replace
execute as @e[tag=normalchest] at @s run setblock ~ ~ ~ chest{LootTable:"maze:normalchest"} replace

schedule function maze:refreshchests 20s
