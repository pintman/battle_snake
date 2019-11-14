import bottle
import json

@bottle.post("/start")
def start():
    print("start")
    js = bottle.request.json
    print(js)
    return {
        "color": "#ff00ff",
        "headType": "bendr",
        "tailType": "pixel"
    }

@bottle.post("/move")
def move():
    print("move")
    js = bottle.request.json
    print(js)

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
    
