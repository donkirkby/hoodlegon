from turtle import *  # @UnusedWildImport


def hexagon(depth, target, size):
    for i in range(6):
        forward(size)
        right(60)
        if (i % 2) != 3 and depth < target:
            tilt = 15
            right(tilt)
            offset = size*.6
            back(offset)
            hexagon(depth+1, target, size*.7)
            forward(offset)
            left(tilt)
    if depth == target:
        # fillcolor((0, depth*0.2, 0))
        down()
        begin_fill()
        for _ in range(6):
            forward(size)
            right(60)
        end_fill()
        up()


def draw_all():
    fillcolor('white')
    pensize(2)
    up()
    back(window_width()/2 - 200)
    left(90)
    back(window_height()/2 - 340)
    right(90)
    for target in reversed(range(4)):
        hexagon(depth=0, target=target, size=100)


def main():
    tracer(0)
    draw_all()
    update()
    mainloop()


if __name__ == '__main__':
    main()
elif __name__ == '__live_coding__':
    x = 1
    draw_all()
