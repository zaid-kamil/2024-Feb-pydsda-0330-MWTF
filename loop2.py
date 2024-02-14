from turtle import *
speed('fastest')

n = 0
while n <= 200:
    fd(100 + n)
    rt(60)
    write(n)
    n += 2

hideturtle()
mainloop()