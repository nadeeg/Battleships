import json
from http.server import HTTPServer, BaseHTTPRequestHandler

import Constants

class RequestHandler(BaseHTTPRequestHandler):
    game_engine = None

    def do_GET(self):
        content_len = int(self.headers.get('Content-Length'))
        get_body = self.rfile.read(content_len)
        
        if self.path == "/startGame":
            json_body = json.loads(get_body)

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            player_id = self.game_engine.register_player()
            if player_id == Constants.FULL:
                self.wfile.write(str.encode(json.dumps({'status':
                                                        Constants.FULL,
                                                        'player_id': -1})))
            else:
                self.wfile.write(str.encode(json.dumps({'status':
                                                        Constants.WAIT,
                                                        'player_id': player_id,
                                                        'rows': Constants.ROWS,
                                                        'cols': Constants.COLS})))
        elif self.path == "/status":
            json_body = json.loads(get_body)

            player_id = json_body['player_id']

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            turn = self.game_engine.get_turn()
            print ("turn given " + str(turn)+ " to player " + str(player_id))

            if turn == Constants.GAME_OVER_LOOSER:
                self.wfile.write(str.encode(json.dumps({'status':
                                                        Constants.GAME_OVER_LOOSER})))
            else:
                if turn == Constants.WAIT or turn != player_id: 
                    self.wfile.write(str.encode(json.dumps({'status': Constants.WAIT})))
                else: 
                    self.wfile.write(str.encode(json.dumps({'status': Constants.PLAY})))

        elif self.path == "/play":
            status = Constants.WAIT 
            shot = Constants.MISS
            json_body = json.loads(get_body)

            player_id = json_body['player_id']
            x = json_body['x']
            y = json_body['y']

            output = self.game_engine.play(player_id, x, y)
            if output[0]:
                shot = Constants.HIT
            if output[1]:
                status = Constants.GAME_OVER_WINNER

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            self.wfile.write(str.encode(json.dumps({'status': status,
                                                    'shot': shot})))
