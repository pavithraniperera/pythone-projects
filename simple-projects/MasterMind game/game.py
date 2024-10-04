import random  # Importing the random module to generate random choices

# Defining the available colors and game settings
colors = ["R", "B", "G", "Y", "W", "O"]  # List of colors to choose from
tries = 10  # Number of attempts allowed
code_length = 4  # Length of the secret code

# Function to generate a random code
def generate_code():
    code = []  # List to hold the randomly chosen colors
    for _ in range(code_length):  # Loop through the length of the code
        color = random.choice(colors)  # Randomly choose a color
        code.append(color)  # Add the color to the code
    return code  # Return the generated code

# Function to take the player's guess
def guess_code():
    while True:  # Infinite loop to get a valid guess
        guess = input("Guess (enter colors separated by spaces): ").upper().split(" ")
        if len(guess) != code_length:  # Check if the guess has the correct number of colors
            print(f"You must guess exactly {code_length} colors.")
            continue  # If not, ask the player to guess again

        # Check if each color in the guess is valid
        for color in guess:
            if color not in colors:
                print(f"Invalid color {color}. Try again!")
                break  # If any invalid color is found, break the loop
        else:
            break  # If all colors are valid, exit the loop
    return guess  # Return the valid guess

# Function to check how many positions are correct
def check_code(guess, real_code):
    correct_pos = 0  # Number of correct positions
    incorrect_pos = 0  # Number of correct colors in wrong positions
    color_count = {}  # Dictionary to count occurrences of each color in the real code

    # Count the occurrences of each color in the real code
    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    # First pass: Count correct positions
    for i in range(code_length):
        if guess[i] == real_code[i]:  # If the guessed color is in the correct position
            correct_pos += 1  # Increment correct position count
            color_count[guess[i]] -= 1  # Decrement the count of that color

    # Second pass: Count incorrect positions
    for i in range(code_length):
        if guess[i] != real_code[i] and guess[i] in color_count and color_count[guess[i]] > 0:
            incorrect_pos += 1  # Increment incorrect position count
            color_count[guess[i]] -= 1  # Decrement the count of that color
    return correct_pos, incorrect_pos  # Return the counts

# Main function to run the game
def game():
    print(f"Welcome to Mastermind! You have {tries} tries to guess the code.")
    print("The valid colors are:", ', '.join(colors))  # Display the valid colors

    code = generate_code()  # Generate the secret code
    # Uncomment this line if you want to see the secret code (for testing)
    # print("Secret Code:", code)

    # Loop through the allowed number of tries
    for attempt in range(1, tries + 1):
        guess = guess_code()  # Get the player's guess
        correct_pos, incorrect_pos = check_code(guess, code)  # Check the guess

        # If the player guesses the code correctly, they win
        if correct_pos == code_length:
            print(f"Congratulations! You guessed the code in {attempt} attempts.")
            break  # End the game
        # Otherwise, provide feedback on how close they are
        print(f"Correct positions: {correct_pos}, Incorrect positions: {incorrect_pos}")

    # If the player runs out of attempts, reveal the code
    else:
        print(f"Sorry, you ran out of tries. The correct code was: {', '.join(code)}")

# Run the game if this script is executed
if __name__ == "__main__":
    game()
