# ジャンケン
# https://python.atelierkobato.com/janken/

# [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


import random


def judge(x, y):
    score = (x - y + 3) % 3
    if score == 0:
        j = "draw"
    elif score == 1:
        j = "you lose"
    else:
        j = "you win"
    print(j)


hand = ["グー", "チョキ", "パー"]

x = input("手を選んでください\n0:guu, 1:choki, 2:paa\n\n")

x = int(x)

y = random.randint(0, 2)

print("your hand: {}".format(hand[x]))
print("cp hand: {}\n".format(hand[y]))

judge(x, y)
