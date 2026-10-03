from turtle import *

speed (2)
pensize(2)
#kedeli
color ("red")
penup()
goto(50,0)
pendown()

forward(100)
left (90)
forward(100)
left (90)
forward(100)
left (90)
forward (100)


penup()
goto (50,100)
pendown()


#roof
color ("yellow")

begin_fill()

left(150)
forward(100)
right (120)
forward(100)
end_fill()

penup()
goto(80,0)
pendown()



#karebi
color ("gray")
begin_fill()
left(150)
forward(50)
right(90)
forward(40)
right (90)
forward (50)
end_fill()


penup()
goto (55,45)
pendown()

color("blue")
#shusha pirveli
forward (25)
left(90)
forward(20)
left(90)
forward(25)
left(90)
forward(20)

#xazebi pamjarashi

pensize(3)
color("black")

penup()
goto(65,45)
pendown()

left(90)
forward(25)
penup()
goto(55,32)
pendown()
left(90)
forward(20)
pensize(2)
#meore panjara 
penup()
goto(125,45)
pendown()
color("blue")


forward(20)
left(270)
forward(25)
left(270)
forward(20)
left(270)
forward(25)

#gisosebi 2
pensize(3)
color("black")
penup()
goto(135,45)
pendown()
left(180)
forward(25)

penup()
goto(125,32)
pendown()

left(90)
forward(20)
penup ()

#sabas dawera
#s
color("yellow")
goto(-250,200)
pendown()
left(180)
forward(50)
right(270)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward (50)

#A
color("brown")
penup()
goto(-230,100)
pendown()
right(110)
forward(110)
right(140)
forward(110)
penup()
goto(-215,140)
pendown()
right(290)
forward(50)

#b
color("green")
penup()
goto(-130,100)
pendown()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
left(90)
forward(20)
left(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)


#a
color ("blue")
penup()
goto(-60,100)
pendown()

right(110)
forward(110)
right(140)
forward(110)
penup()
goto(-45,140)
pendown()
right(290)
forward(50)

#doneeee
penup()
shapesize(1)

penup()
goto(0,0)
right(360)
right(360)
right(360)
right(360)
right(360)
right(360)
right(360)
right(360)


exitonclick()