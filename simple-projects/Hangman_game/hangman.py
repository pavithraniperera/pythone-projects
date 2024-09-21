import random

words = ["python","java","kotlin","javascript","ruby","swift"]
choosen_word = random.choice(words)
word_display =["_" for _ in choosen_word] #create a list of underscores
attempts = 8  

print("Welcome to Hangman")

while attempts>0 and "_" in word_display:
    print("\n"+" ".join(word_display))
    guess = input("Guess the letter : ").lower()
    if guess in choosen_word :
        for index ,letter in enumerate(choosen_word):
            if letter == guess:
                word_display[index] = guess #reveal letter
                
    else:
        print("That letter doesn't appear in the word") 
        attempts -=1           
if "_" not in word_display:
    print("You guessed the word") 
    print(" ".join(word_display)) 
else:
    print("sorry you didnt guess the word")      
    
    
# words: A list of programming languages.
# choosen_word: This variable holds a randomly selected word from the words list using random.choice().

# word_display = ["_" for _ in choosen_word]
# This creates a list word_display that contains underscores (_) for each letter in the chosen word. For example, if the chosen word is "java," word_display would start as ['_', '_', '_', '_'].
# while attempts > 0 and "_" in word_display:
# This loop continues as long as the player has attempts left (attempts > 0) and there are still underscores in word_display (meaning not all letters have been guessed).

# print("\n" + " ".join(word_display))
# This displays the current state of the word, showing correctly guessed letters and underscores for the missing letters.
# " ".join(word_display) joins each character in word_display with a space, making it look more readable like _ _ _ _.

# guess = input("Guess the letter : ").lower()
# The player inputs a letter guess.
# guess.lower() ensures the input is lowercase, making the game case-insensitive.

# if guess in choosen_word:
#     for index, letter in enumerate(choosen_word):
#         if letter == guess:
#             word_display[index] = guess  # reveal letter
# If the guessed letter is in the choosen_word, the program iterates through the word using enumerate() to get both the index and the letter.
# It replaces the corresponding underscore in word_display with the correct letter.

# else:
#     print("That letter doesn't appear in the word")
#     attempts -= 1
# If the guessed letter is not in the word, the player is informed, and attempts are reduced by 1.

# if "_" not in word_display:
#     print("You guessed the word")
#     print(" ".join(word_display))
# else:
#     print("sorry you didnt guess the word")
# After the loop ends, the game checks whether the player has successfully guessed all letters (no underscores remain in word_display).
# If the word is fully guessed, a congratulatory message is shown.
# If the player runs out of attempts without guessing the word, a failure message is displayed.

