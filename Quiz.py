print("Multiple Choice Quiz Game")

score = 0

print("What is x if 2x - 4 = 0?")
print("A. x = 0 B. x = 2 C. x = -2 D. x = 3")
question_1 = input("Answer: ")
if question_1 == "B" or question_1 == "b":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("What is x if 2x - 8 = 0?")
print("A. x = 0 B. x = 2 C. x = -2 D. x = 4")
question_2 = input("Answer: ")
if question_2 == "D" or question_2 == "d":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("What is x if 2x - 12 = 0?")
print("A. x = 0 B. x = 2 C. x = 6 D. x = -2")
question_3 = input("Answer: ")
if question_3 == "C" or question_3 == "c":
    print("Correct")
    score += 1
else:
    print("Incorrect")
print(" ")
print("Quiz Complete")
print(f"\nYour final score is: {score}/3")
