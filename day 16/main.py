from turtle import Turtle, Screen 
from tkinder import *

root = tk.TK()
frame = tk.Frame(root)

#timmy = turtle.Turtle() #if we had only said import turtle instead of the above, we would have to code as seen on this line
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = screen()
print(my_screen.canvheight)
my_screen.exttonclick()


