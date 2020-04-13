from turtle import *
from math import *

axis_width=3
ray_width=3
line_width=2
lens_width=3


def x_axis():
    color('black')
    width(axis_width)
    forward(200)
    backward(400)

def y_axis():
    color('black')
    home()
    right(90)
    broken_line('black',100,5)
    penup()
    home()
    left(90)
    broken_line('black',100,5)

def broken_line(color1,length,dl):
    color(color1)
    l=0;
    pendown()
    while l<length :
        forward(dl)
        penup()
        forward(dl)
        pendown()
       # forward(dl)
        l=l+2*dl

def line(l,color1,x,y,theta):
    width(line_width)
    color(color1)
    width(ray_width)
    up()
    setposition(x,y)
    down()
    setheading(theta)
    fd(l)        
    return position()

def ray(l,color1,x,y,theta):
    color(color1)
    width(ray_width)
    arrow_size=ray_width+5
    up()
    setposition(x,y)
    down()
    setheading(theta)
    fd(l/2)        
    left(90+45)
    fd(arrow_size)
    left(180)
    fd(arrow_size)
    right(90)
    fd(arrow_size)
    left(180)
    fd(arrow_size)
    right(45)
    forward(l/2)
    return position()

def concave(r,theta,line_color,fill_color,x=0,y=0):
    width(lens_width)
    color(line_color,fill_color)
    up()
    setposition(x,y)
    setheading(-90)
    fd(r*sin(radians(theta)/2))
    down()
    [xb,yb]=position()
    setheading(90-theta/2)
    circle(r,theta)
    [xt,yt]=position()
    return [xt,yt,xb,yb]

def convex(r,theta,line_color,fill_color,x=0,y=0):
    width(lens_width)
    color(line_color,fill_color)
    up()
    setposition(x,y)
    setheading(90)
    fd(r*sin(radians(theta)/2))
    down()
    [xb,yb]=position()
    setheading(180+90-theta/2)
    circle(r,theta)
    [xt,yt]=position()

def draw_curve(r,theta,line_color,fill_color):
    color(line_color,fill_color)
    up()
    home()
    setheading(-90)
    fd(r*sin(radians(theta)/2))
    down()
    begin_fill()
    setheading(90-theta/2)
    circle(r,theta)
    setheading(-90)
    fd(r*sin(radians(theta/2)))
   # setheading(180+45)
   # circle(r,90)
    end_fill()
    

y_axis()
#draw_ray(209,'red')
[x,y]=ray(200,'red',10,12,45)
line(20,'black',10,12,0)
write("ppp \u036b \u03b2 \u03b4 t")
ray(200,'blue',x,y,35)
#draw_lens(80,'black','cyan')
#draw_curve(80,90,'black','cyan')
#print(concave(80,50,'black','cyan'))
color('red', 'yellow')
hideturtle()
done()
