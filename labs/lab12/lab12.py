"""
Name: Duha Kanjo
lab 12.py
"""

from random import randint

def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Duha"
    except:
        pass

def read_data(filename):
    infile = open(filename, "r")
    line = infile.readline()
    lst = line.split("")
    return lst

def is_in_linear(value, lst):
    i = 0
    while i < len(lst):
        if i in value:
            i += 1
    if i == len(value):
        return True
    else:
        return False

def good_input():
    x = eval(input("Enter a number from 1 to 10: "))
    while 0 < x <= 10:
        x = eval(input("Number should be between 1 and 10"))
    return x

def num_digits():
    x = eval(input("Enter a positive integer: "))
    while x >= 1:
        m = 0
        while x > 0:
            m += 1
            x // 10
        print(m)
        x = eval((input("Enter a positive integer")))

def hi_lo_game():
    number = randint(1, 100)
    counter = 0
    x = eval(input("Guess a number between 1-100: "))
    while x != number and counter < 7:
        if x > number and counter != 6:
            print("Too high!")
            x = eval(input("Guess a number between 1-100: "))
        elif x < number and counter != 6:
            print("Too low!")
            x = eval(input("Guess a number between 1-100: "))
        counter += 1
    if x == number:
        print("You win in {0} guesses".format(counter))
    else:
        print("You lose. the number was {0}".format(number))


def main():
    main()
