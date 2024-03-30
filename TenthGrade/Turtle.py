from turtle import bgcolor, speed

from turtle import *

bgcolor("Sky Blue")
speed(0)
pensize(3)

pu()
goto(0,-250)

color("yellow","yellow")
begin_fill()
pd()
circle(300)
end_fill()

pu()
goto(0,-335)
pd()
color("brown","chocolate")
begin_fill()

fd(50)
rt(180)
fd(100)
rt(90)
fd(335)
lt(90)
fd(300)
rt(90)
fd(100)
rt(90)
fd(300)
lt(90)
fd(290)
rt(90)
fd(100)
rt(90)
fd(290)
lt(90)
fd(300)
rt(90)
fd(100)
rt(90)
fd(300)
lt(90)
fd(335)

end_fill()


pu()
goto(-4.5,-100)
lt(90)

color("white","white")

begin_fill()

pd()
circle(150)

end_fill()
lt(90)
fd(25)

color("brown")
fd(250)
rt(180)
fd(125)
lt(90)
fd(125)
lt(180)
fd(250)
lt(180)
fd(125)
rt(90)
fd(62.5)

color("dark red","red")
begin_fill()

goto(-229.5,-350)
goto(-4.5,-10.5)
goto(-100,-350)
lt(90)
fd(-129.5)
goto(-4.5,-10.5)
goto(-359,-350)
fd(129.5)
goto(-4.5,-10.5)
goto(-488.5,-350)
fd(129.5)
goto(-4.5,-10.5)

end_fill()

color("navy","blue")
begin_fill()

goto(120,-350)
goto(-4.5,-10.5)
goto(249.5,-350)
rt(180)
fd(129.5)
goto(-4.5,-10.5)
goto(379,-350)
fd(129.5)
rt(180)
goto(-4.5,-10.5)
goto(508.5,-350)
rt(180)
fd(129.5)

end_fill()

hideturtle()
