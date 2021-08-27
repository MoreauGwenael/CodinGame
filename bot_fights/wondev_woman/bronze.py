import sys

class Game():
    board = []
    allies = []
    ennemies = []
    legal_moves = []

    def update(self, board, allies, ennemies, legal_moves):
        self.board = board
        self.allies = allies
        self.ennemies = ennemies
        self.legal_moves = legal_moves
    
    def get_height(self, x, y):
        return int(self.board[y][x])

    def evaluate(self, new_x, new_y, build_x, build_y):
        move = self.get_height(new_x, new_y)
        block = self.get_height(build_x, build_y)
        if block == 3:
            return 10*move - 1
        else:
            return 10*move + block

    def find_best(self):
        best_move = ""
        best_value = -1
        for i in self.legal_moves:
            if i.split()[0] == "PUSH&BUILD":
                best_move = i
                break
            else:
                move = i.split()[2]
                build = i.split()[3]
                new_x, new_y = allies[int(i.split()[1])]
                if 'N' in move:
                    new_y -= 1
                if 'S' in move:
                    new_y += 1
                if 'W' in move:
                    new_x -= 1
                if 'E' in move:
                    new_x += 1
                build_x, build_y = new_x, new_y
                if 'N' in build:
                    build_y -= 1
                if 'S' in build:
                    build_y += 1
                if 'W' in build:
                    build_x -= 1
                if 'E' in build:
                    build_x += 1
                value = self.evaluate(new_x, new_y, build_x, build_y)
                if value > best_value:
                    best_move = i
                    best_value = value
        return best_move


size = int(input())
units_per_player = int(input())
game = Game()

while True:
    board = []
    for i in range(size):
        board.append(input())
    allies = []
    for i in range(units_per_player):
        unit_x, unit_y = [int(j) for j in input().split()]
        allies.append((unit_x, unit_y))
    ennemies = []
    for i in range(units_per_player):
        other_x, other_y = [int(j) for j in input().split()]
        ennemies.append((other_x, other_y))
    legal_actions = int(input())
    legal_moves = []
    for i in range(legal_actions):
        legal_moves.append(input())
    game.update(board, allies, ennemies, legal_moves)

    print(game.find_best())
