from turtle import Turtle

SIZE = 17
FONT = "arial"
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        self.high_score = 0
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.refresh_score()

    def refresh_score(self) -> None:
        self.goto(0, -290)
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=(FONT, SIZE, "normal"))

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(arg="GAME OVER.", align=ALIGN, font=(FONT, SIZE, "normal"))

    
