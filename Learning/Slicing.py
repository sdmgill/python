players = ['charles','martina','michael','florence','eli']
print(players[0:3]) # 0 is the starting index, 3 is the ending index 0,1,2
print(players[1:4]) # 1 is the starting index, 4 is the ending index so 1,2,3 --> still need to consider 0 even though it is skipped. See example below which includes 0
print(players[:4]) # omitting the starting index assumes 0, 4 is the ending index so 0,1,2,3
print(players[2:]) # omitting the ending index assumes the last index, so 2,3,4
print(players[-3:]) # -3 starts 3 from the last index, so 2,3,4. This would always print the last 3 players as the list changes.

# Looping through a slice
print('\n"Here are the first three players on my team"')
for player in players[:3]:
	print(player.title())

