from os import scandir
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 

# Crear el escenario
screen = Screen() #Instanciar el objeto screen o pantalla
screen.setup(width=600, height=600) # Definir tamano pantalla
screen.bgcolor('black') # Definir el color de fondo
screen.title('Programate snake') # Definir el titulo de la ventana

screen.tracer(0) # Quitamos el efecto animacion por defect


# Instanciar objeto Snake
snake = Snake()


# Instanciar objeto Food
food = Food()

# Instanciar objeto scoreboard
scoreboard = Scoreboard()

#Movimientos de la Snake

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update() # actulizamos movimiento
    time.sleep(0.2)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

#Final
screen.exitonclick() 