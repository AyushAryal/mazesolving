import turtle
import turt


def dimension(maze):
    x=0
    y=0
    for row in maze:
        x+=1
        y=0
        for col in row:
            y+=1
    return(x,y)

def drawsqaure(pen,x,y,color):
    pen.pensize(1)
    pen.color("black",color)
    pen.penup()
    pen.begin_fill()
    pen.setposition(x+1,y+1)
    pen.pendown()
    for times in range(4):
        pen.forward(20)
        pen.left(90)
    pen.end_fill()

def printboard(maze,pen,length,bredth):
    x=20
    y=20
    pen.color("red")
    pen.setposition(x,y)
    for row in maze:
        y=(y-20)%(-20*(bredth+1))
        x=0
        line=""
        for col in row:
            x=(x+20)%(20*(length+1))
            if col=="-":
                color="black"
                drawsqaure(pen,x,y,color)
            elif col=="+":
                color="white"
                drawsqaure(pen,x,y,color)
            elif col=="S":
                color="blue"
                drawsqaure(pen,x,y,color)
            else:
                color="green"
                drawsqaure(pen,x,y,color)
                
            

            line=line+col+"  "
        
        print("\n")

def determinestartpoint(maze):
    x=1
    for row in maze:
        y=1
        for col in row:
            if (col=="S"):
                pos=[x,y]
                return(pos)
            else:
                y+=1
        x+=1

pen=turtle.Turtle()
turtle.bgcolor("#f28343")
pen.hideturtle()
pen.pensize(1)
pen.speed(0)

maze=turt.createboard()
length,bredth=dimension(maze)
printboard(maze,pen,length,bredth)
print(determinestartpoint(maze))

pen.getscreen()._root.mainloop() 