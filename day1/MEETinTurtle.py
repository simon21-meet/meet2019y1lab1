import turtle
# Everything that comes after the # is a 
# comment.
# It is a note to the person reading the code.
# The computer ignores it.
# Write your code below here...

turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the position (-200, -100)  on the screen

turtle.pendown() #Put the pen down to start drawing
                
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)
turtle.penup()
turtle.goto(-200+150,100)
turtle.pendown()
turtle.forward(100)





# ...and end it before the next line.
turtle.mainloop() 
# turtle.mainloop() tells the turtle to do all
# the turtle commands above it and paint it on the screen.
# It always has to be the last line of code!



