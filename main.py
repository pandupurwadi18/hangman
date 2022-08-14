# --- Hangman ---
# 100 days of code Python
# Pandu Purwadi 

#import random package
import random
#import word
from replit import clear
from hangman_word import word_list
from hangman_art import stages, logo

end_of_the_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"
    

while not end_of_the_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
      print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_the_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_the_game = True
        print("Congratulation, you win!")
    print(stages[lives])