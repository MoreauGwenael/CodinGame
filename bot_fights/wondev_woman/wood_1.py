import sys


size = int(input())
units_per_player = int(input())

while True:
    for i in range(size):
        row = input()
    for i in range(units_per_player):
        unit_x, unit_y = [int(j) for j in input().split()]
    for i in range(units_per_player):
        other_x, other_y = [int(j) for j in input().split()]
    nb_legal_actions = int(input())
    legal_actions = []
    for i in range(nb_legal_actions):
        inputs = input()
        legal_actions.append(inputs)
        inputs = inputs.split()
        atype = inputs[0]
        index = int(inputs[1])
        dir_1 = inputs[2]
        dir_2 = inputs[3]
        
    print(legal_actions, file=sys.stderr, flush=True)
    print(legal_actions[0])
