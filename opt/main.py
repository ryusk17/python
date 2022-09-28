if False:
    print("hello world")

    name = input("what is your name?")
    print("hello " + name)

    import os

    print(os.getcwd())

    for i in range(4):
        print(i)

# string = input("let's typing anything: ")
# print(string)

height = 200
print("身長は", height, "cmです")
# print("身長は" + height + "cmです") # エラーとなる
print("身長は" + str(height) + "cmです")

# text = "The shells she sells are sea-shells, I'm sure."
# print(text.find("sea"))

# data = 0.5
# print(data.as_integer_ratio())

# print("Python" < "python")
# print("1" < "A")

# age = int(input("hou old r u?"))
# if (age <= 10) or (80 <= age):
#     print("no")
# else:
#     print("yes")

# if not (age < 10):
#     print("yes")

# text = ""
# while text != "finish":
#     text = input("finishと入力してください。: ")
#     print(text, "と入力されました。")

#     if text == "":
#         print("無効")
#         continue

#     if text == "break":
#         print("中断")
#         break
# print("終了")

values = [1, 2, 3, 4]
for value in values:
    print(value)

fruits = {"apple": "red", "grape": "purple", "peach": "pink"}
print(fruits)
for fruit in fruits:
    color = fruits[fruit]
    print(fruit, "の色は", color)
for color in fruits.values():
    print(color)
for fruit, color in fruits.items():
    print(fruit, color)

del fruits["apple"]
print(fruits)
print("apple" in fruits)


yellow = (255, 255, 0)  # タプル
print(0 in yellow)
r, g, b = yellow
print(r, g, b)

list_obj = [1, 2, 3]
var1, var2, var3 = list_obj
print(var1, var2, var3)


# 関数名を引数にできる
def abc(f):
    f()
    f()


def f():
    print("hello")


abc(f)


def three(a, b, c):
    print(a, b, c)


def do_four(f, a, b, c):
    f(a, b, c)


print(dict([("abc", 123), ("xyz", 987)]))

string1, string2, string3 = "", "", "b"
print(string1 or string2 or string3)

print(dir())
print(__name__)
