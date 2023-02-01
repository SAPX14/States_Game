import turtle

image = "map.gif"
turtle.addshape(image)
turtle.shape(image)


def coordinates(x, y):
    print(x, y)


turtle.onscreenclick(coordinates)
turtle.mainloop()
