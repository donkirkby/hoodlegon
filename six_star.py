from turtle import *  # @UnusedWildImport


def hexagon(size, depth):
    for _ in range(6):
        forward(size)
        right(60)
        draw(depth-1, size-25)


def draw(depth, size):
    if depth == 0:
        return
    hexagon(size, depth)


def draw_all():
    pensize(2)
    up()
    back(window_width()/2 - 100)
    right(90)
    forward(window_height()/2 - 320)
    left(90)
    down()
    draw(4, 175)


def main():
    tracer(0)
    draw_all()
    update()
    mainloop()


if __name__ == '__main__':
    main()
elif __name__ == '__live_coding__':
    draw_all()
