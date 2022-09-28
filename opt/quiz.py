# quiz
# https://www.askpython.com/python/examples/easy-games-in-python


print("welcome to Quiz")

answer = input("are your ready? (y/n) :")
score = 0
total_questions = 3

if answer.lower() == "y":
    answer = input("Q1: what is your favourite programing language?\n")
    if answer.lower() == "python":
        score += 1
        print("correct")
    else:
        print("wrong answer")

print("Thank you for playing quiz game, you attempted", score, "question correctly!")
mark = (score / total_questions) * 100
print("Marks obtained: ", mark)
