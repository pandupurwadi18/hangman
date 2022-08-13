# --- Hangman ---
# 100 days of code Python
# Pandu Purwadi 

import random

word_list = ["cook","swim","sleep","work","eat","drink"]

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

lives = 6

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

end_of_the_game =  False

while not end_of_the_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 0
        if lives == 0:
            end_of_the_game = True
            print("You lose.")

    print(display)

    if "_" not in display:
        end_of_the_game = True
        print("Congratulation, you win!")