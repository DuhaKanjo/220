"""
Name: Duha Kanjo
<ProgramName>.py
"""
from random import randint

def get_words(in_file):
    infile = open(in_file, "r")
    lines = infile.readlines()
    x = []
    for line in range(len(lines)):
        word_list = x.append()
        return word_list


def pick_words(word):
    rand = randint(0, len(word))
    return rand


def guessedWord(secret_word, wrong_letters, guessed_word, letter):
    check = False
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            guessed_word[i] = letter
            check = True
    if check == True:
        return True
    wrong_letters.append(letter)
    return False


def wordSpelled(guessed_word, secret_word):
    if "".join(guessed_word) == secret_word:
        return True
    else:
        return False

def guess_letter(wrong_letters, secret_word, guessed_word):
    user_input = input("Enter the guessed letter")
    user_input = user_input.lower()
    for ch in wrong_letters:
        while user_input == ch:
            user_input = input("Enter the guessed letter")
    if guessed_word(secret_word, wrong_letters, guessed_word, user_input):
        return True
    else:
        False


def printBoard(guessed_word, turn_count, guessed_letters):
        print(" the guessed word is", len(guessed_word))
        print(guessed_word)
        print("the turn_count is", str(turn_count))
        print(" guessed letters are", str(guessed_letters))



def playGame():
    word = get_words("word.txt")
    secret_word = pick_words(word)
    guessed_word = [" "] * len(secret_word)
    guessed_letters = []
    turn_count = 0
    printBoard(guessed_word, turn_count, guessed_letters)
    while turn_count < 7 and not wordSpilled(guessed_word, secret_word, guessed_word):
        if guessLetter(guessed_letters, turn_count, secret_word, guessed_word) == False:
            turn_count +=1
            printBoard(guessed_word, turn_count, guessed_letters)
    if turn_count >= 7:
        print("Run out of Turns, Game is over")
    else:
        print(" Congrats!! You won")







def main():



main()
