import re

import requests
from constants import WALL_DX, WALL_DY, N_COLS, N_ROWS
from wall import create_wall


def create_maze():
    """Create wall objects from the maze returned by the web service."""
    wall_list = []
    response = requests.post(
        'https://www.delorie.com/game-room/mazes/genmaze.cgi',
        data={'cols': N_COLS, 'rows': N_ROWS, 'type': 'text'},
        timeout=10,
    )
    response.raise_for_status()
    match = re.search(r'<pre>\s*(.*?)\s*</pre>', response.text, re.DOTALL)
    if match is None:
        raise ValueError("Maze service response did not contain maze data.")

    y = 0
    for line in match.group(1).splitlines():
        x = 0
        for character in line:
            if character != ' ':
                wall_list.append(create_wall(x, y, WALL_DX, WALL_DY))
            x += WALL_DX
        y += WALL_DY
    return wall_list