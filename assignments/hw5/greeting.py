"""
Duha Kanjo
greeting.py
certification of authenticity:
I certify that this assignment is entirely my own work.
"""
import time
from graphics import GraphWin, Point, Polygon, Text, Line

def main():
    win = GraphWin("greeting card", 500, 500)
    point1 = Point(250, 125)
    point2 = Point(310, 90)
    point3 = Point(370, 125)
    point4 = Point(310, 250)
    point5 = Point(250, 375)
    point8 = Point(190, 90)
    point7 = Point(130, 125)
    point6 = Point(190, 250)
    heart = Polygon(point1, point2, point3, point4, point5, point6, point7, point8)
    heart.draw(win)
    heart.setFill("Red")
    point1.draw(win)
    point2.draw(win)
    point3.draw(win)
    point4.draw(win)
    point5.draw(win)
    point6.draw(win)
    point7.draw(win)
    point8.draw(win)
    text = Text(Point(250, 425), "Happy Valentine's Day")
    text.setFace("helvetica")
    text.setStyle("bold italic")
    text.setSize(20)
    text.setTextColor("purple")
    text.draw(win)
    start_point = Point(60, 400)
    arrow = Line(start_point, Point(150, 300))
    arrow.setArrow("last")
    arrow.draw(win)
    for _ in range(20):
        arrow.move(15, -15)
        time.sleep(0.5)
    arrow.undraw()
    text2 = Text(Point(250, 50), "Click anywhere to close")
    text2.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
