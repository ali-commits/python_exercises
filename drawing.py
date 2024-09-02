import turtle

pen = turtle.Turtle()

while True:
    shape = input("Enter the shape (circle/square/polygon) or 'quit' to stop: ")
    if shape == "quit":
        break

    color = input("Enter the color: ")
    pen.color(color)

    if shape == "circle":
        radius = int(input("Enter the radius: "))
        pen.circle(radius)
    elif shape == "square":
        side = int(input("Enter the side length: "))
        for _ in range(4):
            pen.forward(side)
            pen.right(90)
    elif shape == "polygon":
        sides = int(input("Enter the number of sides: "))
        side = int(input("Enter the side length: "))
        for _ in range(sides):
            pen.forward(side)
            pen.right(360 / sides)


turtle.done()
