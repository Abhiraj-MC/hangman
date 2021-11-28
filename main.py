import os
import random
import time


def clear():
    os.system('cls')  # clear console


if not os.path.isfile('words.xd'):  # checks for the wordsxd file ie. words library
    yesno = input("words.xd not found. do you want to download the words library? [y/n] ")

    if yesno.lower() == 'y':
        print("working on it...")
        os.system('python gitgetwordsxd.py')
        print("done. going to game.")
        time.sleep(5)
        clear()
    else:
        print("then u cant play the game xd")

words = open("words.xd", "r")
content = words.readlines()

chosen_word = random.choice(content)
chosen_word = chosen_word.lower()
chosen_word = chosen_word.strip()  # imports the library into a list, chooses a random word, strips it and lowers it.

guesses_left = 7
guessed_letters = []
game_over = False

while not game_over:

    print("Hangman.py")
    print("----------------------")
    print()
    print("Your word looks like: ")
    for letter in chosen_word:
        if letter.lower() in guessed_letters:
            print(letter, end='')
        else:
            print('_', end='')
    print('')  # basically prints the word with found letters and _ instead of missing letters.

    print('Guesses left: ' + str(guesses_left))
    print('')
    current_guess = input("Your next guess: ")  # take guess

    if current_guess == 'gimme da ans':  # cheat 8)
        print("ohk here u go")
        print(chosen_word)
        guesses_left += 1

    if current_guess == '69420 pls gimme them guesses':  # cheat 8)
        print("sure")
        guesses_left += 69420

    if current_guess == 'quit':  # quit
        print("quitting")
        break

    guessed_letters.append(current_guess.lower())  # adds the letter to guessed letters list

    if current_guess.lower() not in chosen_word:  # wrong guess
        guesses_left -= 1
        print("Wrong guess. you lost a guess")
        if guesses_left == 0:  # no guesses left, game lsot
            break
    else:
        print("Correct guess.")

    game_over = True

    for letter in chosen_word:
        if letter.lower() not in guessed_letters:  # checks if any letters and un guessed with guesses left, thus game is not over yet
            game_over = False

    time.sleep(2)
    clear()

if game_over:
    print(f"gg u won.")
    print("the word was " + chosen_word)
    print("you had " + str(guesses_left) + " guesses left.")
else:
    print('')
    print("game over. you lost. the word was " + str(chosen_word))

print("exiting in 3 seconds")
time.sleep(3)
