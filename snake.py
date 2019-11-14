import bottle
import json
import random

 # https://docs.battlesnake.com/snake-api#tag/endpoints/

@bottle.post("/start")
def start():
    print("start")
    js = bottle.request.json
    print(js)

    return {
        "color": "#ff00ff",
        "headType": "pixel",  # "beluga" "bendr" "dead" "evil" "fang" "pixel" "regular" "safe" "sand-worm" "shades" "silly" "smile" "tongue" 
        "tailType": "pixel" # "block-bum" "bolt" "curled" "fat-rattle" "freckled" "hook" "pixel" "regular" "round-bum" "sharp" "skinny" "small-rattle" 
    }

@bottle.post("/move")
def move():
    print("move")
    js = bottle.request.json
    print(js)
    return {
        "move": random.choice(["up", "down", "left", "right"])
    }

@bottle.post("/end")
def end():
    print("end")
    js = bottle.request.json
    print(js)

@bottle.post("/ping")
def ping():
    print("ping")
    js = bottle.request.json
    print(js)


def main(host, port):
    bottle.run(host=host, port=port)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("python snake.py HOST PORT")
        sys.exit()

    host, port = sys.argv[1:3]
    main(host, int(port))
    
