import turtle

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.flowables import Flowable

import hyacinth
from pdf_turtle import PdfTurtle
import sea_star
import six_star


class TurtleArt(Flowable):
    def __init__(self, draw_func, width, height):
        self.draw_func = draw_func
        self.width = width
        self.height = height

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)

    def draw(self):
        t = PdfTurtle(self.canv, width=self.width, height=self.height)
        turtle.Turtle._screen = t.screen
        turtle.Turtle._pen = t
        self.draw_func()


def go():
    doc = SimpleDocTemplate("hoodlegon.pdf")
    story = []
    story.append(TurtleArt(sea_star.draw_all, 475, 560))
    story.append(TurtleArt(six_star.draw_all, 380, 500))
    story.append(TurtleArt(hyacinth.draw_all, 500, 600))
    doc.build(story)

go()

# Uncomment this to display the PDF after you generate it.
# from subprocess import call  # @IgnorePep8
# call(["evince", "hoodlegon.pdf"])
