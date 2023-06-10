scoreboard objectives add gamephase dummy
scoreboard objectives add spawntimer dummy
scoreboard objectives add starttimer dummy
scoreboard objectives add numplayers dummy
scoreboard objectives add readytogetitems dummy
scoreboard objectives add numkeys dummy "Keys"
scoreboard objectives add winner dummy

team add players
team modify players friendlyFire false

execute unless score #maze gamephase matches 0..5 run scoreboard players set #maze gamephase 0
