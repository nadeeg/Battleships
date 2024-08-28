import time
from http.server import HTTPServer 
from RequestHandler import RequestHandler
from GameEngine import GameEngine

from GameSession import GameSession

import Constants

if __name__ == '__main__':
    RequestHandler.game_engine = GameEngine(Constants.ROWS, Constants.COLS, Constants.SHIPS)
    game_server = HTTPServer((Constants.HOST_NAME, Constants.PORT_NUMBER), RequestHandler)
    
    # print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        game_server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    game_server.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (Constants.HOST_NAME, Constants.PORT_NUMBER))
