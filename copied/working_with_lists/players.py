# slicing items in a list
players = ['charles', 'kenn', 'aden', 'chali', 'eli', 'simo']
print(f" welcome {players[0].upper()} to this tournament!")
print(players[0:4])
print(players[-2:])
print("here are the first three players")
for player in players[:3]:
    print(player.title())
