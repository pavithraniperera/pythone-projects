import time

questions = [
    {
        "prompt": "What is the capital of France?",
        "Options": ["A: Paris", "B: London", "C: Berlin", "D: Colombo"],
        "Answer": "A",
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "Options": ["A: Spanish", "B: Portuguese", "C: English", "D: Korean"],
        "Answer": "B",
    },
    {
        "prompt": "What is the smallest prime number?",
        "Options": ["A: 1", "B: 2", "C: 3", "D: 5"],
        "Answer": "B",
    },
]


def run_quiz(questions, time_limit):
    
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["Options"]:
            print(option)

        # Start timer
        start_time = time.time()

        # Ask for input and check for time limit
        try:
            answer = input_with_timer("Enter your answer: ", time_limit).upper()
        except TimeoutError:
            print(f"Time's up! The correct answer was {question['Answer']}\n")
            continue

        # Check if answer is correct
        if answer == question["Answer"]:
            print("Your answer is correct!!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer was {question['Answer']}\n")

    print(f"Your total score out of {len(questions)}: {score}")


def input_with_timer(prompt, time_limit):
    # Get input within the time limit
    start_time = time.time()
    answer = input(prompt)
    if time.time() - start_time > time_limit:
        raise TimeoutError
    return answer


# Run the quiz with a 15-second time limit for each question
run_quiz(questions, time_limit=15)

# This code defines a simple quiz program that asks multiple-choice questions and checks the user's answers. Here's a breakdown of how it works:

# questions List:

# This list contains multiple dictionaries, where each dictionary represents a question. Each dictionary has:
# prompt: The question being asked.
# Options: The available answer choices.
# Answer: The correct option.
# run_quiz Function:

# The function run_quiz(questions) runs the quiz. It:
# Initializes the score to 0 to keep track of correct answers.
# Loops through each question in the questions list:
# Prints the question (prompt) and all the answer choices (Options).
# Asks the user to input their answer using input().
# Compares the user's input to the correct answer (Answer). If it's correct, the user gets a point; if not, the correct answer is shown.
# After all the questions are asked, the total score is printed.
# Explanation of input() and upper:

# The line answer = input("Enter your Answer :").upper is meant to get the user's input and convert it to uppercase.
# final Output:

# The function displays the user's score at the end, showing how many questions they answered correctly.
