import turtle

def make_window(col, titl):
    """
    Setup up the window with the given background color (col) and title (titl).
    Returns the new window
    """
    w = turtle.Screen()
    w.bgcolor(col)
    w.title(titl)
    return w

def make_turtle(col, pensz):
    """
    Set up a new turtle of color (col) and pensize (pensz).
    Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(col)
    t.pensize(pensz)
    return t 

def draw_concentric_square(t, sz):
    """
    Draw a square using turtle t of side length sz.
    """
    for i in range(4):
        t.forward(sz)
        t.left(90)

    # move to the new starting postion for the next square
    t.penup()
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.pendown()

# set up a window and a turtle

wn = make_window("lightgreen", "Drawing 5 concentric squares")
alex = make_turtle("red", 3)
side_length = 20

# draw 5 squares

for i in range(5):
    draw_concentric_square(alex, side_length) 
    side_length = side_length + 40 # increase the side length of the square for the next sqare

    
wn.mainloop()
   