import turtle

import svgwrite

import hyacinth
import sea_star
import six_star
from svg_turtle import SvgTurtle


def write_file(draw_func, filename, size):
    drawing = svgwrite.Drawing(filename, size=size)
    drawing.add(drawing.rect(fill='white', size=("100%", "100%")))
    t = SvgTurtle(drawing)
    turtle.Turtle._screen = t.screen
    turtle.Turtle._pen = t
    draw_func()
    drawing.save()


def main():
    write_file(hyacinth.draw_all, 'hyacinth.svg', size=("500px", "500px"))
    write_file(sea_star.draw_all, 'sea_star.svg', size=("475px", "460px"))
    write_file(six_star.draw_all, 'six_star.svg', size=("380px", "350px"))
    print('Done.')


if __name__ == '__main__':
    main()
