# https://python.softmoco.com/basics/python-try-except.php

val1 = 1
val2 = 2

try:
    print(val1 / val2)
except:
    print("error")

try:
    print(val1 / val2)
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("error")

try:
    print(val1 / val2)
except Exception as e:
    print(e)

try:
    print(val1 / val2)
except Exception as e:
    print(e)
else:
    print("no error")
finally:
    print("done")
