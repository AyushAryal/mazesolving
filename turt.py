import turtle
import time
pen=turtle.Turtle()
pen.shape("circle")
pen.pensize(3)


pen.setposition(0,1)
pen.down()
pen.color("green")
pen.forward(100)
pen.up()

pen.setposition(0,20)
pen.down()
pen.color("blue")
pen.forward(100)
pen.up()

pen.setposition(0,30)
pen.down()
pen.color("green")
pen.forward(100)
pen.up()

pen.setposition(0,40)
pen.down()
pen.color("red")
pen.forward(100)


pen.getscreen()._root.mainloop() 


