from turtle import Screen
from my_snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=590, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 12:
        food.refresh()
        scoreboard.increase_score()  
        snake.extend()
# game over through wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        
        scoreboard.reset()
        snake.reset()
# game over by tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 15:
                scoreboard.reset()
                snake.reset()

screen.exitonclick()