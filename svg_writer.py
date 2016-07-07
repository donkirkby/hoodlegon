import turtle

import svgwrite

from svg_turtle import SvgTurtle


def draw(t):
    t.fillcolor('blue')
    t.begin_fill()
    for i in range(20):
        d = (50 + i*i*1.5)
        t.pencolor(0, 0.05*i, 0)
        t.width(i)
        t.forward(d)
        t.right(144)
    t.end_fill()
    t.right(90)
    t.up()
    t.pencolor('black')
    t.write('Hello, World!',
            font=('Courier', 20, 'italic'))
    t.forward(20)
    t.write('Hello, World!',
            font=('Courier', 20))
    t.forward(20)
    t.write('Hello, World!',
            font=('Courier', ))
    t.forward(20)
    t.write('Hello, World!',
            font='Courier')
    t.forward(20)
    t.write('Hello, World!')
    t.forward(20)
    t.write('Hello, World!', align='left')
    t.forward(20)
    t.write('Hello, World!', align='center')
    t.forward(20)
    t.write('Hello, World!', align='right')
    t.forward(20)


def main():
    drawing = svgwrite.Drawing('test.svg', size=("800px", "600px"))
    t = SvgTurtle(drawing)
    draw(t)
    drawing.save()
    print('Done.')


def main2():
    turtle.tracer(0)
    draw(turtle)
    turtle.update()
    turtle.mainloop()

if __name__ == '__main__':
    main()
elif __name__ == '__live_coding__':
    draw(turtle)
