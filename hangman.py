import random
import string

from wordlist import word_list

output_word = ""
alphabet = list(string.ascii_uppercase)
available_letters = list(string.ascii_uppercase)
used_letters = []


def hangman(word_list, out_word):
    # pick a word
    word = random.choice(word_list).upper()
    print(word)

    # fill shown word
    for i in range(len(word)):
        out_word += "*"

    # starts game
    strikes = 0
    game_over = False
    while not game_over:
        found = False
        user_letter = get_letter(out_word, strikes)

        # check if letter is in the given word
        for i in range(len(word)):
            if word[i] == user_letter:
                out_word = out_word[:i] + user_letter + out_word[i + 1:]
                found = True

        if found:
            print("You got it right")
            if word == out_word:
                print("You won!!! The word was " + word)
                game_over = True
        else:
            print("It was wrong")
            strikes += 1
            if strikes == 5:
                print("You failed :( The word was " + word)
                game_over = True


def get_letter(out_word, strike_num):
    # interface
    print("\nWord to guess is: ", end="")
    for letter in out_word:
        print(letter, end=" ")
    print("\nUsed letters are:", *used_letters, end=" ")
    print("\nAvailable letters are: ", *available_letters, end=" ")
    print("\nYou have other " + str(5 - strike_num) + " strikes left")
    user_input = input("\nGuess a letter\t").upper()
    print("")
    if user_input in used_letters:
        print("***************************************")
        print("LETTER ALREADY GUESSED, TRY ANOTHER ONE")
        print("***************************************")
        get_letter(out_word, strike_num)
    elif user_input not in alphabet:
        print("***************************************")
        print("INPUT INVALID, YOU CAN ONLY USE LETTERS")
        print("***************************************")
        get_letter(out_word, strike_num)
    else:
        available_letters.remove(user_input)
        used_letters.append(user_input)
        print("You guessed " + user_input)
        return user_input


hangman(word_list, output_word)
