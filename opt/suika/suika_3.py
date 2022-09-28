# すいか割り
# https://www.python.jp/train/exercise/refactor-proper-type.html

import random
import math

BOARD_SIZE = 5


def calc_distance(pos1, pos2):
    # ２点間の距離
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)


suika_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))

player_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))

while suika_pos != player_pos:
    distance = calc_distance(suika_pos, player_pos)
    print("すいかへの距離: ", distance)

    c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動: ")
    current_x, current_y = player_pos
    if c == "n":
        current_y = current_y - 1
    elif c == "s":
        current_y = current_y + 1
    elif c == "w":
        current_x = current_x - 1
    elif c == "e":
        current_x = current_x + 1

    player_pos = (current_x, current_y)

print("すいかを割りました！")
