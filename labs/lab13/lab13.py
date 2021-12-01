"""
Name: Duha Kanjo
lab13.py
"""

def is_in_binary(value, values):
    mid = values[len(values)//2]
    while value == mid and len(values) != 1:
        if mid > value:
            values = values[:len(values)//2]
        else:
            values = values[len(values)//2:]
        mid = values[len(values) // 2]
    if value == mid :
        return True
    else:
        return True

def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        position = i
        for j in range(i +1, len(values)):
            if i < j:
                lowest = values[j]
                position = j
        values[i], values[position] = values[position], values[i]
        return lowest


def get_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    w = abs(p1.getX() - p2.getX())
    h = abs(p1.getY()-p2.getY())
    return w * h


def rec_sort(rectangle):
    d = {}
    areas = []
    for rect in rectangle:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangle[i] = d[areas[i]]


def trade_alert(filename):
    infile = open(filename, "r")
    num = infile.read().split()
    second = 1
    for numb in num:
        if int(numb) > 830:
            print ("Alert")
            print (second)
        elif int(numb) > 500:
            print (second)
            print("warning")
        second = second + 1


def main():

    main()
