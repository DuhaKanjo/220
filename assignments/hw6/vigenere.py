"""
Duha Kanjo
vigenere.py
certification of authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import*


def main():
    win = GraphWin("Vigenere", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    Text(Point(0.5, 3), "Message to code").draw(win)
    Text(Point(0.5, 2.50), "Enter Keyword").draw(win)
    entry_box = Entry(Point(2.25, 3), 20).draw(win)
    entry_box2 = Entry(Point(2.25, 2.50), 20).draw(win)
    Rectangle(Point(1, 1), Point(2, 1.5)).draw(win)
    Text(Point(1.5, 0.5), "Click Anywhere to close").draw(win)
    encode_it = Text(Point(1.5, 1.25), "Encode").draw(win)
    message = entry_box.getText()
    keyword = entry_box2.getText()
    output_text = Text(Point(2.25, 1), '')
    output_text.draw(win)
    win.getMouse()
    encode_it.undraw()
    encoded = code(message, keyword)
    Text(Point(1.5, 1.75), " resulting message\n" + encoded)
    win.getMouse()
    win.close()


def code(message, key):
    message = message.upper()
    message = message.split()
    message = "".join(message)

    key = key.upper()

    m = message
    k = key
    key.upper()
    acc = ''
    for i in range(len(m)):
        x = m[i]
        y = k[i % len(k)]
        y = ord(y) - 65
        z = ord(x) + y
        if z > 90:
            z -= 26
        c = chr(z)
        acc += c
    return acc


if __name__ == '__main__':
    main()
