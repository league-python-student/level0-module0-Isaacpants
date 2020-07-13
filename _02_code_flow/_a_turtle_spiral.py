import random
import turtle
from _curses import COLOR_GREEN

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    isaac = turtle.Turtle()
    # This code sets our shape to a turtle
    isaac.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    isaac.speed(2)
    # Set your turtle's color using .color('green')
    isaac.color('green')
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        # Set the turtle color to a random color
        isaac.color(getRandomColor())
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        isaac.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        isaac.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        isaac.width(i)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
