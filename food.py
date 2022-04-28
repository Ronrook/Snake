from turtle import Turtle
import random


class Food(Turtle): #Crear clase Food, la herencia es entre parentesis, en este caso desde Turtle (padre)
    
    def __init__(self): #Definir constructor
        super().__init__() #hereda todo de Turtle 
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.refresh()
        

    # Generar Food de forma aleatorio en la Screen
    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y) 