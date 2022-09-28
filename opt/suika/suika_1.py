# すいか割り
# https://www.python.jp/train/exercise/index.html

import random
import math


def calc_distance(x1, y1, x2, y2):
    # ２点間の距離
    diff_x = x1 - x2
    diff_y = y1 - y2

    return math.sqrt(diff_x**2 + diff_y**2)


suika_x = random.randrange(0, 5)
suika_y = random.randrange(0, 5)

player_x = random.randrange(0, 5)
player_y = random.randrange(0, 5)

while (suika_x != player_x) or (suika_y != player_y):
    distance = calc_distance(player_x, player_y, suika_x, suika_y)
    print("すいかへの距離: ", distance)

    c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動: ")
    if c == "n":
        player_y = player_y - 1
    elif c == "s":
        player_y = player_y + 1
    elif c == "w":
        player_x = player_x - 1
    elif c == "e":
        player_x = player_x + 1

print("すいかを割りました！")
