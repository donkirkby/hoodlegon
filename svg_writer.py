import turtle

import svgwrite

import six_star
from svg_turtle import SvgTurtle


def main():
    size = ("380px", "350px")
    drawing = svgwrite.Drawing('six_star.svg', size=size)
    drawing.add(drawing.rect(fill='white', size=size))
    t = SvgTurtle(drawing)
    turtle.Turtle._screen = t.screen
    turtle.Turtle._pen = t
    six_star.draw_all()
    drawing.save()
    print('Done.')


if __name__ == '__main__':
    main()
