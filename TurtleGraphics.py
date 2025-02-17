#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(sam, sides):
    for s in range(sides):
        sam.forward(50)
        sam.right(360/sides)
        
def fillCorner(felipe, corner):
    #draw big square
    drawSquare(felipe, 100)
    
    if corner == 1:
        felipe.begin_fill()
        drawSquare(felipe, 50)
        felipe.end_fill()
    elif corner ==2:
        felipe.forward(50)
        felipe.begin_fill()
        drawSquare(felipe, 50)
        felipe.end_fill()
    elif corner == 3:
        felipe.forward(100)
        felipe.right(90)
        felipe.forward(50)
        felipe.beginfill()
        drawSquare(felipe,50)
        felipe.end_fill()
    elif corner == 4:
        felipe.forward(100)
        felipe.right(90)
        felipe.forward(100)
        felipe.right(90)
        felipe.forward(50)
        felipe.beginfill()
        drawSquare(felipe,50)
        felipe.end_fill()
        
    
def main():
    myTurtle = turtle.Turtle()
    
    # drawSquare(myTurtle,100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    # drawPolygon(myTurtle,3)
    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
def squaresinSquares(doc, squares) :
    cool = -199
    dude = 199
    for o in range(squares):
        doc.penup()
        doc.goto( cool, dude)
        drawSquare(doc,dude *2)
        cool = cool + 10
        dude = dude - 10
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
