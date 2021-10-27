"""
Name: Duha Kanjo
lab9.py
"""
from graphics import*
import math


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squresEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])
def writeSumOfSquares():
    file = input(" Enter the name of file: ")
    infile = open(file, "r")
    outfile = open("outfile", "w+")
    for line in infile:
        line = line.split()
        toNumbers(line)
        squresEach(line)
        s = sumList(line)
        outfile.write("The sum is: " + str(s))

def starter():
    weight = eval(input("Enter your weight "))
    wins = eval(input("enter numbers of wins"))

    if 150 <= weight < 160:
        if wins >= 5:
            print(" Player earned a starting position")
    elif weight > 199 or wins > 20:
        print("Player is a starter")
    else:
        print("Player didn't earn the starting position")
def leapYear(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print(str(year) + "is a leap year")
    else:
        print(str(year) + "is not a leap year")

def circle():
    win = GraphWin("Circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    circle1 = Circle(p1, radius1)
    circle1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)

    if distance <= (radius1 + radius2):
        print("The circle overlap")
    else:
        print("the circle do not overlap")
    win.getMouse()
    win.close()



def main():
    addTen([1,2,3])
    writeSumOfSquares()
    starter()
    leapYear(2008)
    circle()







main()
