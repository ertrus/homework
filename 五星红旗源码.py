import turtle as t

#参数设置
t.setup(600,400,0,0)
t.bgcolor("red")
t.fillcolor("yellow")
t.color('yellow')
t.speed(5)
#主星
t.begin_fill()
t.up()
t.goto(-260,100)
t.down()
for i in range (5):
    t.forward(150)
    t.right(144)
t.end_fill()

#第1颗副星
t.begin_fill()
t.up()
t.goto(-110,180)
t.setheading(300)
t.down()
for i in range (5):
    t.forward(50)
    t.left(144)

t.end_fill()


#第2颗副星
t.begin_fill()
t.up()
t.goto(-350,212)
t.setheading(30)
t.down()
for i in range (5):
    t.forward(50)
    t.right(144)

t.end_fill()

#第3颗副星
t.begin_fill()
t.up()
t.goto(-350,145)
t.setheading(5)
t.down()
for i in range (5):
    t.forward(50)
    t.right(144)

t.end_fill()

#第4颗副星
t.begin_fill()
t.up()
t.goto(-400,90)
t.setheading(300)
t.down()
for i in range (5):
    t.forward(50)
    t.left(144)

t.end_fill()

t.done()
