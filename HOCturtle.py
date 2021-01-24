import turtle as t
import random

def get_line_length():
    choice = input(" 'Enter line length(long, medium, short': ")




    print (choice)

    if choice == 'long' :
        line = 250
    elif choice == 'medium' :
        line = 200
    else:
        line = 50

    return line
def get_line_width():
    choice = input('Enter line width "superthick, thick, thin": ')
    
    print(choice)
    if choice == 'superthick':
        line = 40
    elif choice == 'thick':
        line = 25
    else:
        line = 5
    return line
        



line_length = get_line_length()
print('THe return value is', line_length)

line_width = get_line_width()
print('The return value is', line_width)

def move_turtle(line_length):
    pen_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    t.pencolor(random.choice(pen_color))
    t.shapesize(3, 3, 1)
    t.stamp()


    t.right(45)
    t.forward(line_length)


t.penup()
t.goto(0, 100)
t.pendown()
t.fillcolor('yellow')
t.pensize(line_width)
t.forward(line_length)


move_turtle(line_length)

while True:
    move_turtle(line_length)
    

















