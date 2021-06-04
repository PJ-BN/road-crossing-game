import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()


screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
touch = (60, 30)

while game_is_on:

    time.sleep(0.1)
    screen.update()
    for i in range(1):
        car.move()
        screen.update()
        for k in car.cars:
            if player.distance(k) < 30:
                game_is_on = False
                score.game_over()
                screen.update()
                pass

    for j in range(-250, 250):
        if player.distance(j, 280) < 10:
            player.refresh()
            score.level_up()
            car.increase()

    time.sleep(0.1)
    car.new_one()



screen.exitonclick()
