import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []

class Balle():
    def __init__(self):
        cercle_change_x = 3
        cercle_change_y = 3
        self.cercle_x = cercle_change_x
        self.cercle_y = cercle_change_y
        self.rayon_cercle = random.randint(10,30)

    def on_update(self):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(10, 10, 20, (255, 54, 34))


import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []





class rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rayon = random.randint(10, 30)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.angle = random.randint(3, 150)
        self.vitesse_x = random.randint(-100, 100)
        self.vitesse_y = random.randint(-100, 100)

    def changement_vitesse(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.rayon, self.angle, self.color, 45)





class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.list_circle = []
        self.list_rectangle = []
        self.flag = True
        self.vitesse = 100
        pass

    def setup(self):
        pass



    def on_mouse_press(self, x=int, y=int, button=int, modifiers=int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            rayon = random.randint(10, 30)
            color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            vitesse_x = random.randint(-100, 100)
            vitesse_y = random.randint(-100, 100)
            self.list_circle.append([x, y, rayon, color, vitesse_x, vitesse_y])
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.list_rectangle.append(rectangle(x, y))


    def on_draw(self):
        arcade.start_render()
        for circle in self.list_circle:
            arcade.draw_circle_filled(circle[0], circle[1], circle[2], circle[3])
        for rectangle in self.list_rectangle:
            rectangle.draw()
        arcade.finish_render()


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


main()
