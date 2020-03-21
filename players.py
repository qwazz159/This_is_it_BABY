players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
'prints a slice of the three, charles martina and michael'

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
'automatically does the first 4 without defining first value'

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
'does michael after'

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
	print(player.title())
