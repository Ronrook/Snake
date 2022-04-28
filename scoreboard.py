
from tkinter import font
from turtle import Turtle

ALIGN = "center"
FONT= ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self): 
        super().__init__() #hereda todo de Turtle 
        self.score = 0 # Atributo
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"El puntaje es: {self.score}", font=FONT, align= ALIGN)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"¡El Juego terminado! su puntaje es: {self.score}", font=FONT, align= ALIGN)