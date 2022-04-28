from turtle import Turtle, xcor

STARTING_POSITIONS= [(0,0),(-20,0),(-40,0)]
UP = 90
RIGHT = 0
DOWN = 270
LEFT =  180



class Snake:

    def __init__(self):
        self.segments = [] #Atributo
        self.create_snake() #Metodo
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle('square')
            snake_segment.color('white')
            snake_segment.penup()
            snake_segment.goto(position) # metodo goto sirve para mover la serpiente en diferentes coordenadas
            self.segments.append(snake_segment)
        



    def move(self):    
        for seg_num in range(len(self.segments) -1, 0,-1):
            new_x= self.segments[seg_num - 1].xcor()
            new_y= self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(20)
        #self.head.left(90)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

