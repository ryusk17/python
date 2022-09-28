# リスト型

# https://docs.python.org/ja/3/tutorial/datastructures.html#list-comprehensions

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# ↓と等価
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)


# https://docs.python.org/ja/3/tutorial/datastructures.html#nested-list-comprehensions

matrix = [[1, 2, 3, 4][5, 6, 7, 8][9, 10, 11, 12]]
# 行と列を入れ替える
print([[row[i] for row in matrix] for i in range(4)])
