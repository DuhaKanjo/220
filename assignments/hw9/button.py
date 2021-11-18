"""
name: Duha Kanjo
Three doors game
problem: creating a user_defined class
I certify that this assignment is entirely my own work.
"""
from graphics import Text


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        click_x = point.getX()
        click_y = point.getY()

        point_1_x = self.shape.getP1().getX()
        point_1_y = self.shape.getP1().getY()

        point_2_x = self.shape.getP2().getX()
        point_2_y = self.shape.getP2().getY()
        if point_1_x <= click_x <= point_2_x and point_1_y <= click_y <= point_2_y:
            return True
        return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
