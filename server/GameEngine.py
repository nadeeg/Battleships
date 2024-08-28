import uuid

import Constants
from GameSession import GameSession

CURR_TURN = Constants.PLAYER1_ID

class GameEngine:
    def __init__(self, rows, cols, num_ships):
        # only support one session
        self.session = GameSession(rows, cols, num_ships)
        self.player_count = 0;

    def register_player(self):
        # only suppport two players
        if self.player_count == 0:
            self.player_count = 1
            return Constants.PLAYER1_ID
        elif self.player_count == 1:
            self.player_count = 2
            return Constants.PLAYER2_ID
        else:
            return Constants.FULL

    def get_turn(self):
        if self.player_count == 2:
            return CURR_TURN
        else:
            return Constants.WAIT

    def play(self, player_id, x, y):
        global CURR_TURN

        other_player = Constants.PLAYER1_ID

        if player_id == Constants.PLAYER1_ID:
            other_player = Constants.PLAYER2_ID

        updates = self.session.update_map(other_player, x,y)

        if updates[1]:
            CURR_TURN = Constants.GAME_OVER_LOOSER
            return updates 

        else:
            if player_id == Constants.PLAYER1_ID:
                CURR_TURN = Constants.PLAYER2_ID
            else:
                CURR_TURN = Constants.PLAYER1_ID

            return updates

