"""
Name: Duha Kanjo
lab 6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """

    name = input("Please enter your first and last name? ")
    name = name.split(" ")
    print(name[1] + "," + name[0])

def company_name():
    y = input(" Enter a three_part internet domain name? ")
    company = y.split(".")
    print(company[1] + ".")

def initials():
    a = eval(input("How many students are in this class?"))
    for i in range(a):
        first = input("enter first name of student" + str(i+1) + ":")
        last = input("enter last name:")
        print(first + "'s initials are" + " " + first[0] + last[0] + ".")
def names():
    x = input("Enter people's names, separated by commas: ")
    names = x.split(", ")
    print("The initials are", end=" ")
    for name in names:
        name = name.split(" ")
        print(name[0][0] + name[1][0], end=" ")
def thirds():
    n = eval(input("How many sentences will be input ?"))
    for _ in range(n):
        x = input("Enter the sentences ")
        print(x[2::3])

def word_average():
    sentences = input(" Enter the sentence ")
    acc = 0
    words = sentences.split(" ")
    for word in words:
        acc = acc + len(word)
        print(acc/len(words))

def pig_latin():
    x = input(" Enter the sentence")
    x.lower()
    words = x.split(" ")
    print(x, "->", end=" ")
    for word in words:
        y = word[1:] + word[0] + "ay"
        print(y, end=" ")

def main():
    name_reverse()
    company_name()
    initials()
    names()
    word_average()
    thirds()
    pig_latin()
main()
