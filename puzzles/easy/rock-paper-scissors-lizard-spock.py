import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rules = {
    'R': 'LC',
    'P': 'RS',
    'C': 'PL',
    'L': 'SP',
    'S': 'CR'
}
players = []

n = int(input())
for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    players.append((numplayer, signplayer, []))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

while len(players) > 1:
    next_turn_players = []

    while len(players):
        player_1 = players.pop(0)
        player_2 = players.pop(0)

        if player_1[1] == player_2[1]:
            if player_1[0] < player_2[0]:
                player_1[2].append(player_2[0])
                next_turn_players.append(player_1)
            else:
                player_2[2].append(player_1[0])
                next_turn_players.append(player_2)
        elif player_2[1] in rules[player_1[1]]:
            player_1[2].append(player_2[0])
            next_turn_players.append(player_1)
        else:
            player_2[2].append(player_1[0])
            next_turn_players.append(player_2)

    players = next_turn_players

print(players[0][0])
print(*players[0][2])
