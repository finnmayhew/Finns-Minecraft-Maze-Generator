execute as @p[scores={winner=1}] run tellraw @a {"text":"","color":"white","extra":[{"selector":"@s"},{"text":" wins!"}]}
scoreboard players set #maze gamephase 5
