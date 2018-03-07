import random

scores = [];
print("Scores and Grades")
for item in range(0,10):
    scores.append(random.randint(60, 100))
    for score in scores:
        if (score >= 90):
            grade = "A"
        elif (89 >= score >= 80):
            grade = "B"
        elif (79 > score >= 70):
            grade = "C"
        elif (69 >= score >= 60):
            grade = "D"

    print("Score: " + str(score) + "; Your grade is " + grade)