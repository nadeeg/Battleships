import random
import uuid

class GameSession:
    def __init__(self, rows, cols, num_ships):
        self.id = str(uuid.uuid4())
        # set the maps
        self.player1_map = [[0]*cols for _ in [0]*rows]
        self.player2_map = [[0]*cols for _ in [0]*rows]

        self.maps = dict()
        self.maps[1] = self.player1_map
        self.maps[2] = self.player2_map

        self.ship_c = dict()
        self.ship_c[1] = num_ships
        self.ship_c[2] = num_ships

        # set the ships for player 1
        print("player 1")
        for x in range(num_ships):
            rand_x = random.randint(0,rows-1)
            rand_y = random.randint(0,cols-1)

            self.player1_map[rand_x][rand_y] = 1
            print(str(rand_x) + "," + str(rand_y))

        print("player 2")
        for x in range(num_ships):
            rand_x = random.randint(0,rows-1)
            rand_y = random.randint(0,cols-1)

            self.player2_map[rand_x][rand_y] = 1
            print(str(rand_x) + "," + str(rand_y))

    def get_player1_map(self):
        return self.player1_map

    def get_player2_map(self):
        return self.player2_map

    def get_id(self):
        return self.id

    def update_map(self, player_id, x, y):
        curr_map = self.maps[player_id]
        sucsess = False
        won = False

        if curr_map[x][y] == 1:
            sucsess = True
            curr_map[x][y] = -1
            self.ship_c[player_id] = self.ship_c[player_id] - 1
            if self.ship_c[player_id] == 0:
                won = True

        return (sucsess, won)
