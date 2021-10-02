'''CREATE TASK:
IDEA: Implement December Canvas Project but allow list indexing for colors, shapes, and sizes)
Implement more options of colors shapes and sizes as well
Build from scratch'''
#ADD LIST ELEMENTS TO THE IF AND RESET LIST FUNCTIONS
import turtle
wn=turtle.Screen()
wn.setup(width=1200, height=700)
wn.bgcolor("black")
#create lists and variables that will be used in this project
rainbow_colors=["red", "orange", "yellow","green","blue","violet","white"]
rainbow_colors_index_number=-1
size_list=[1,2,3,4]
size_list_index_number=0
pen_size_list=[1,7,15,30]
pen_size_list_index_number=0
shape_list=["arrow", "circle","turtle","triangle","square","classic"]
shape_list_index_number=0
angle_variable=45 
pen_counter=3
font_information=("Verdana",20,"normal")
idea_list=["House","Boat","Rocket","Star"]
idea_index_number=0
#creates the turtles that will be used in this project
#sample_size=turtle.Turtle()
#sample=turtle.Turtle()
controls_and_info=turtle.Turtle()
idea_turtle=turtle.Turtle()
controls_and_info.ht()
controls_and_info.pencolor(rainbow_colors[6])
controls_and_info.pu()
controls_and_info.goto(-500,300)
controls_and_info.pd()
controls_and_info.write("Controls: Q-Pen Up/Down, W-Color, E-Size, R-Shape, S-Stamp, C-Clear", font=font_information)
controls_and_info.pu()
idea_turtle.pu()
idea_turtle.ht()
idea_turtle.pencolor(rainbow_colors[6])
idea_turtle.goto(-100,255)
idea_turtle.pd()
font_information= ("Verdana",15,"normal")
command_key="Draw a " + idea_list[idea_index_number]
idea_turtle.write(command_key, font=font_information)
pen=turtle.Turtle()
pen.pencolor(rainbow_colors[6])
pen.color((rainbow_colors[6]))
pen.setheading(90)
#creates sign that writes the controls header and then writes the control information
#create the movement of the painter
def right_turn():
    pen.right(angle_variable)
def left_turn():
    pen.left(angle_variable)
def forward():
    pen.forward(100)
def pen_up_and_down():
    global pen_counter
    pen_counter=pen_counter+1 
    #print(pen_counter)
    if (pen_counter%2)==0:
        pen.penup()
    else:
        pen.pendown()
def clear_canvas():
    pen.ht()
    pen.pu()
    pen.clear()
    pen.goto(0,0)
    pen.st()
    pen.pd()
    pen.setheading(90)
    global pen_counter
    pen_counter=3
    global idea_index_number
    idea_index_number=idea_index_number+1
    global command_key
    #print(idea_index_number)
    command_key=("Draw a " + idea_list[idea_index_number])
    idea_turtle.clear()
    idea_turtle.write(command_key, font=font_information)
    #print(command_key)
    if idea_index_number==len(idea_list)-1:
        idea_index_number=-1 
def change_color():
    global rainbow_colors_index_number
    rainbow_colors_index_number=rainbow_colors_index_number+1
    pen.pencolor(rainbow_colors[rainbow_colors_index_number]) 
    pen.color(rainbow_colors[rainbow_colors_index_number])
    if rainbow_colors_index_number==len(rainbow_colors)-1: 
        rainbow_colors_index_number=-1
def size_change():
    global size_list_index_number
    global pen_size_list_index_number
    size_list_index_number=size_list_index_number+1
    pen_size_list_index_number=pen_size_list_index_number+1
    pen.shapesize(size_list[size_list_index_number])
    pen.pensize(pen_size_list[pen_size_list_index_number])
    if size_list_index_number and pen_size_list_index_number == len(pen_size_list)-1:
        size_list_index_number=-1 
        pen_size_list_index_number=-1
def shape_change():
    global shape_list_index_number
    shape_list_index_number=shape_list_index_number+1
    pen.shape(shape_list[shape_list_index_number])
    if shape_list_index_number== len(shape_list)-1:
        shape_list_index_number=-1
def stamp():
    pen.stamp()
wn.onkeypress(right_turn, "Right")
wn.onkeypress(left_turn, "Left")
wn.onkeypress(forward,"Up")
wn.onkeypress(pen_up_and_down, "q")
wn.onkeypress(clear_canvas, "c")
wn.onkeypress(change_color,"w")
wn.onkeypress(size_change,"e")
wn.onkeypress(shape_change,"r")
wn.onkeypress(stamp,"s")
wn.listen()
wn.mainloop()