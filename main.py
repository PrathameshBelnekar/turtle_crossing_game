import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
Tim = Player()
cars = CarManager()

screen.listen()
screen.onkey(Tim.go_up, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    
    for car in cars.all_cars:
        if Tim.distance(car) < 20:
            game_is_on = False
    
    if Tim.is_at_finishline():
        Tim.go_to_start()
        cars.level_up()

    
screen.exitonclick()







