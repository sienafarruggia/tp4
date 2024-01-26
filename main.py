#TP4
#2024
#By khalil Bendjennet et Siena Farruggia

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []


#La classe des balles
class balle():
    def __init__(self,x,y):
        #circle variables
        self.cercle_change_x = 3
        self.cercle_change_y = 3
        self.cercle_x = x
        self.cercle_y = y
        self.cercle_rayon = random.randint(10,100)
        self.cercle_couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #to make the circles move without them getting out of frame
    def on_update(self):
        self.cercle_x += self.cercle_change_x
        self.cercle_y += self.cercle_change_y
        if self.cercle_x < self.cercle_rayon:
            self.cercle_change_x *=-1
        if self.cercle_x > SCREEN_WIDTH - self.cercle_rayon:
            self.cercle_change_x *=-1
        if self.cercle_y < self.cercle_rayon:
            self.cercle_change_y *=-1
        if self.cercle_y > SCREEN_HEIGHT - self.cercle_rayon:
            self.cercle_change_y *=-1

    #to draw the circles
    def on_draw(self):
        arcade.draw_circle_filled(self.cercle_x, self.cercle_y, self.cercle_rayon, self.cercle_couleur)


#La classe des rectangles
class rectangle():
    def __init__(self, x, y):
        #rectangle variables
        self.change_x = 3
        self.change_y = 3
        self.rectangle_x = x
        self.rectangle_y = y
        self.width = random.randint(10,200)
        self.height = random.randint(10,200)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    #to make the rectangles move without them getting out of frame
    def on_update(self):
        self.rectangle_x += self.change_x
        self.rectangle_y += self.change_y
        if self.rectangle_x < (self.width/2):
            self.change_x *= -1
        if self.rectangle_x > SCREEN_WIDTH - (self.width/2):
            self.change_x *= -1
        if self.rectangle_y < (self.height/2):
            self.change_y *= -1
        if self.rectangle_y > SCREEN_HEIGHT - (self.height/2):
            self.change_y *= -1

    #to draw the rectangles
    def draw(self):
        arcade.draw_rectangle_filled(self.rectangle_x, self.rectangle_y, self.width, self.height, self.color)


#La classe de MyGame
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.list_circle = []
        self.list_rectangle = []

    def setup(self):
        pass

    #to make shapes appear when you click the mouse
    def on_mouse_press(self, x=int, y=int, button=int, modifiers=int):
        #to make a circle appear when you click the left side of the mouse
        if button == arcade.MOUSE_BUTTON_LEFT:
            circle1 = balle(x,y)
            self.list_circle.append(circle1)
        #to make a rectangle appear when you click the right side of the mouse
        if button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle1 = rectangle(x,y)
            self.list_rectangle.append(rectangle1)

    #to draw the shapes
    def on_draw(self):
        arcade.start_render()
        for circle in self.list_circle:
            circle.on_draw()
        for rectangle in self.list_rectangle:
            rectangle.draw()
        arcade.finish_render()

    #to make the shapes move
    def on_update(self, delta_time: float):
        for circle in self.list_circle:
            circle.on_update()
        for rectangle in self.list_rectangle:
            rectangle.on_update()

def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


main()
