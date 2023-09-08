from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def main() -> None:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.title("Snake Game")
    
    snake = Snake() 
    food = Food()
    scoreboard = Scoreboard()

    is_game_on = True

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    while(is_game_on):
        snake.move_snake()
        screen.update()
        time.sleep(0.1)

        if snake.head.distance(food) < 19:
            food.refresh()
            scoreboard.score += 1
            scoreboard.refresh_score()
            snake.extend()

        if abs(snake.head.xcor()) >= 275 or abs(snake.head.ycor()) >= 280:
            is_game_on = False

        for segment in snake.snake_segments[1:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False 
    
    scoreboard.game_over()

    screen.exitonclick()

main()
