# alt + shift + down -> duplicate line
from turtle import *
pencolor('red')
pensize(3)
speed('fastest')
for i in range(10):
    fd(120)
    lt(360/10)
    write(i, font=('Calibri', 25))
hideturtle()
mainloop()
