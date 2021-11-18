"""
Name: Duha Kanjo
button.py
certification of authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
from button import Button
from graphics import GraphWin, Rectangle, Point, Text


def main():
    win = GraphWin("Three Door Game", 500, 500)

    text = Text(Point(250, 100), "I have a secret door")
    instructions = Text(Point(250, 400), "Click to choose my door")
    text.draw(win)
    instructions.draw(win)

    door_1_rect = Rectangle(Point(50, 300), Point(150, 350))
    door_1 = Button(door_1_rect, "Door 1")
    door_1.draw(win)

    door_2_rect = Rectangle(Point(200, 300), Point(300, 350))
    door_2 = Button(door_2_rect, "Door 2")
    door_2.draw(win)

    door_3_rect = Rectangle(Point(350, 300), Point(450, 350))
    door_3 = Button(door_3_rect, "Door 3")
    door_3.draw(win)

    user_click = win.getMouse()
    door_1_clicked = door_1.is_clicked(user_click)
    door_2_clicked = door_2.is_clicked(user_click)
    clicked_button = door_1

    if door_1_clicked:
        message = did_win(door_1)
    elif door_2_clicked:
        message = did_win(door_2)
        clicked_button = door_2
    else:
        message = did_win(door_3)
        clicked_button = door_3

    if message == "You win":
        clicked_button.color_button("green")
        message = Text(Point(250, 400), message)
        instructions.undraw()
        message.draw(win)
    else:
        clicked_button.color_button("red")
        message = Text(Point(250, 400), "click to close")
        message.draw(win)

    click_message = Text(Point(250, 450), "click to close")
    click_message.draw(win)

    win.getMouse()
    win.close()


def get_random():
    random = randint(1, 3)
    return random


def did_win(cl_button):
    win_door = get_random()

    if int(cl_button.get_label()[-1]) == win_door:
        return "You Win!"
    else:
        return "Sorry, you lose!" + str(win_door) + "was the secret door"


main()
