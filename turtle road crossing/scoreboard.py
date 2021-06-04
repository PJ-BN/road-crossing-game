from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-250, 250)
        self.level = 0
        self.level_up()

    def level_up(self):
        level_score = f"Level {self.level}"
        self.clear()
        self.write(level_score, font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(-30, 0)
        self.write("GAMEOVER", font=FONT)