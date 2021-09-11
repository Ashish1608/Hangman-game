import random
from hangman_words import word_list
from hangman_art import stages, logo
import os

def clear(): return os.system('cls')

actual_word = random.choice(word_list)
word_length = len(actual_word)
lives = 6

user_word = []

for letter in actual_word:
    user_word += '_'

# print(actual_word)
# print(user_word)

print(logo)

Game_over = False

while not Game_over:
    user_guess = input("\nGuess a letter: ")
    clear()
    print(logo, "\n")

    if user_guess in user_word:
        print(f"\nYou've already guessed {user_guess}!")

    for position in range(word_length):
        if actual_word[position] == user_guess:
            user_word[position] = user_guess

    if user_guess not in actual_word:
        lives -= 1
        print(
            f"\nYou guessed {user_guess}, that's not in the word. You lose a life.\n")

        if lives == 0:
            Game_over = True
            print("You lose!")

    print(' '.join(user_word), "\n")

    if '_' not in user_word:
        Game_over = True
        print("You Win!")

    print(stages[lives])
