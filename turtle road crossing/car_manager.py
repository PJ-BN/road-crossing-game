from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 40
MOVE_INCREMENT = 20


class CarManager:

    def __init__(self):
        self.cars = []
        self.make()
        self.starting_speed = STARTING_MOVE_DISTANCE

    def make(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(1, 2)
        colo = random.choices(COLORS)
        new_car.color(colo)
        x_cord = 290
        y_cord = random.randint(-200, 200)
        new_car.goto(x_cord, y_cord)

        self.cars.append(new_car)

    def move(self):
        for i in range(len(self.cars)):

            self.cars[i].backward(self.starting_speed)

    def increase(self):
        self.starting_speed += MOVE_INCREMENT

    def new_one(self):
        # time.sleep(2)
        self.make()

