import turtle

import svgwrite

import six_star
from svg_turtle import SvgTurtle


def main():
    drawing = svgwrite.Drawing('six_star.svg', size=("380px", "350px"))
    t = SvgTurtle(drawing)
    turtle.Turtle._screen = t.screen
    turtle.Turtle._pen = t
    six_star.draw_all()
    drawing.save()
    print('Done.')


if __name__ == '__main__':
    main()
