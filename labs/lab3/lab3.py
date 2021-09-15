"""
Name: Duha Kanjo
lab3.py
"""

def average():
    grades = eval(input(" how many grade do you have"))
    acc = 0
    for i in range(grades):
        x = eval(input("enter your grade on HW" + str(i+1)))
        acc = acc + x
    answer = acc/grades
    print(answer)

def tip_jar():
    acc = 0
    for i in range(5):
        total = eval(input("how much do you want to donate?"))
        acc += total
    print(acc)

def newton():
    x = eval(input(" what the number x is "))
    refine = eval(input("How many times to improve the approximation?"))
    approximation = x/2
    for i in range(refine):
        approximation = (approximation + (x/approximation))/2
    print(approximation)

def sequence():
    x = eval(input("enter the number of terms in a series "))
    for i in range(1, x+1):
        print(1+(i//2*2))

def pi():
    x = eval(input("enter the number of terms in the series"))
    acc = 1
    for i in range(x):
        num = (2+(i//2*2))
        den = (1+(i+1)//2*2)
        acc *= num/den
    print(acc * 2)
