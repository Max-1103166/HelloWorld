games = [
    "Player’s Unknown Battle Ground (PUBG) 50 Million 2018",
    "Fortnite Battle Royal 39 Million 2017",
    "Apex Legends 50 Million (1 Month) 2019",
    "League of Legends (LOL) 27 Million 2009",
    "Counter Strike; Global Offensive 32 Million 2014",
    "Heartstone 29 Million 20120",
    "Minecraft 91 Million 2011",
    "DOTA 2 5 million 2015",
    "The Division 2 N/A 2019",
    "The Splatoon 2",
]

print(f"5 {games[4]}")
print(len(games[7]))
print(f"Er zijn {games.count} games in deze lijst")
games.insert(1, "Snake")
print(f"Helaas heeft de game {games[10]} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {games[10]}.")
games.pop()
games[6] = "Heartstone 29 Million 2012"
print(games)