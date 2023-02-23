import turtle

wn = turtle.Screen()
wn.title("Pokemon Catcher")
wn.bgcolor("black")

wn.register_shape("pokeball.gif")

pokeball = turtle.Turtle()
pokeball.shape("pokeball.gif")
pokeball.speed(0)

clicks = 0

mark = turtle.Turtle()
mark.hideturtle()
mark.color("white")
mark.penup()
mark.goto(0, 300)
mark.write(f"Capture the pokemon!: {clicks}", align = "center", font = ("Courier New", 32, "normal"))

def click(x,y):
    global clicks
    clicks += 1
    mark.clear()
    mark.write(f"Capture the pokemon!: {clicks}", align = "center", font = ("Courier New", 32, "normal"))
pokeball.onclick(click)


wn.mainloop()


