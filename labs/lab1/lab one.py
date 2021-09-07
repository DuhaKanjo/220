"""
Name: <Duha Kanjo>
labl.py

problem: this function calculates the area of a rectangle
"""

def calc_rec_area():
     length = eval (input ("Enter the length:"))
     width =eval (input ("Enter the width:"))
     area = length * width
     print ("Area =", area)

def calc_volume():
    length = eval(input("Enter the length:"))
    width =eval (input ("Enter the width:"))
    height =eval (input ("Enter the height: "))
    volume = length * width * height
    print ("volume=", volume)

def shooting_percentage():
    made= eval(input("Enter the made:"))
    took= eval(input("Enter the took"))
    percent= made/took * 100
    print ("percentage=", percentage)

def cofee():
    pound = eval(input("Enter the pound:"))
    fixed= eval (input("Enter the fixed:"))
    coffee= 10.50 * pound + 0.86 * pound + 1.50
    print ("coffee=", coffee)


def  kilometer_to_mile():
    mile= eval(input("Enter the mile"))
    kilometer= eval(input("Enter the kilometer"))
    mile = 1.61 * kilometer
    print ("mile=", mile)
