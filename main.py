# --- Hangman ---
# 100 days of code Python
# Pandu Purwadi 

import random

word_list = ["cook","swim","sleep","work","eat","drink"]

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")