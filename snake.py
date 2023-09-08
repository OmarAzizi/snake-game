from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self) -> None:
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def reset(self) -> None:
        for segment in self.snake_segments:
            segment.goto(1000,100)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
     
    def create_snake(self):
        for i in range(3):
            self.snake_segments.append(Turtle("square"))
            self.snake_segments[i].penup()
            self.snake_segments[i].color("indianred1")
            self.snake_segments[i].goto(x=-20 * i, y=0)

    def move_snake(self) -> None:
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_pos = self.snake_segments[seg_num -  1].position()
            self.snake_segments[seg_num].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)
    
    def add_segment(self, position) -> None:
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("indianred1")
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self) -> None:
        self.add_segment(self.snake_segments[-1].position())

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(270)
    
    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(0)

