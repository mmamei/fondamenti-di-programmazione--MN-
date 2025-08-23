import requests
from constants import WALL_DX,WALL_DY,N_COLS,N_ROWS
from wall import create_wall


def create_maze():
    wall_list = []
    maze = requests.post('http://www.delorie.com/game-room/mazes/genmaze.cgi',
                          data={'cols': N_COLS, 'rows': N_ROWS, 'type': 'text'})
    y = 0
    for l in maze.text.splitlines():
        if not l.startswith('<'):
            x = 0
            for c in l:
                if c != ' ':
                    wall_list.append(create_wall(x, y, WALL_DX, WALL_DY))
                x += WALL_DX
            y += WALL_DY
    return wall_list