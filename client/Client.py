
import http.client
import json
import time

import Constants

def start_game(connection):
    global player_id
    global rows
    global cols
    global other_map
    headers = {'Content-type': 'application/json'}
    req_body = {'op': Constants.START_GAME}
    req_body_json = json.dumps(req_body)
    
    connection.request("GET", "/startGame", req_body_json, headers)
    response = connection.getresponse()

    rsp_json = json.loads(response.read().decode())

    if rsp_json['status'] == Constants.WAIT:
        player_id = rsp_json['player_id']
        rows = rsp_json['rows']
        cols = rsp_json['cols']
        other_map =  [['.']*cols for _ in ['.']*rows]
        return Constants.WAIT 

    return -1

def wait(connection):
    while True:
        headers = {'Content-type': 'application/json'}
        req_body = {'op': Constants.WAIT, 'player_id': player_id}
        req_body_json = json.dumps(req_body)
        connection.request("GET", "/status", req_body_json, headers)

        response = connection.getresponse()
        rsp_json = json.loads(response.read().decode())

        if rsp_json['status'] == Constants.WAIT:
            time.sleep(3)
        elif rsp_json['status'] == Constants.GAME_OVER_LOOSER:
            print("game over, you lost, better luck next time")
            quit()
        else:
            break

def play(connection):
    global other_map
    print_other_map()
    while True:
        try:
            x = int(input("get x coordinate : "))
        except ValueError:
            continue

        if x < 0 or x > rows - 1:
            continue

        break

    while True:
        try:
            y = int(input("get y coordinate : "))
        except ValueError:
            continue

        if y < 0 or y > cols - 1:
            continue

        break
    
    headers = {'Content-type': 'application/json'}
    req_body = {'op': Constants.PLAY, 'player_id': player_id, 'x': x, 'y': y}
    req_body_json = json.dumps(req_body)
    connection.request("GET", "/play", req_body_json, headers)
    
    response = connection.getresponse()
    rsp_json = json.loads(response.read().decode())

    if rsp_json['shot'] == Constants.HIT:
        print("that was a direct hit")
        other_map[x][y] = 'x'

    if rsp_json['status'] == Constants.GAME_OVER_WINNER:
        print("game over! you are the winner")
        quit()


def print_other_map():
    for i in range(cols+1):
        if i == 0:
            print("  ", end="")
        else:
            print(str(i-1) + " ", end="")
    print("")
    for i in range(rows):
        print(str(i) + " ", end="")
        for j in range(cols):
            print(other_map[i][j] + " ", end="")
        print("")
    print("")

player_id = -1
rows = -1
cols = -1

other_map = None

HOST_NAME = "localhost"
PORT_NUMBER = 8080

connection = http.client.HTTPConnection(HOST_NAME, PORT_NUMBER)

if start_game(connection):
    while True:
        wait(connection)
        play(connection)
