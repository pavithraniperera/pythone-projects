questions = [
    {
        "prompt": "What is the capital of france ?",
        "Options": ["A: Paris", "B: London", "C: Berlin", "D: Colombo"],
        "Answer": "A",
    },
    {
        "prompt": "Which language is primarily spoke in Brazil ?",
        "Options": ["A: Spanish", "B: Prutugees", "C: English", "D: Korean"],
        "Answer": "B",
    },
    {
        "prompt": "What is the smallest prime number ?",
        "Options": ["A: 1", "B: 2", "C: 3", "D: 5"],
        "Answer": "B",
    },
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["Options"]:
            print(option)
        answer = input("Enter your Answer :")
        if answer == question["Answer"]:
            print("Your answer is correct !!")
            score += 1
        else:
            print("Sorry you got the wrong answer. The correct Answer was "+question["Answer"])
    print(f"Your total score out of {len(questions)} :" + str(score))


run_quiz(questions)
