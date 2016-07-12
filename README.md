Inspired by [Occupy Math][occupy], a set of colouring pages based on hexagons.
It seemed like a good project to try out my [Live Coding in Python][live] tools.

My favourite is the three-legged sea star:

![Sea Star][sea_star]

My second favourite reminds me of a hyacinth flower:

![Hyacinth][hyacinth]

This six-pointed star was interesting, because the code was so simple:

![Six-pointed Star][six_star]

Here's the code for the six-pointed star:

    from turtle import *
    
    
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

Notice that I just draw hexagons, and the star emerges from the overlaps.

Feel free to use any of the images or code. Let me know if you find other
interesting patterns.

[occupy]: https://occupymath.wordpress.com/2016/07/04/image-of-the-week-8/
[live]: http://donkirkby.github.io/live-py-plugin/
[sea_star]: https://rawgit.com/donkirkby/hoodlegon/master/sea_star.svg
[six_star]: https://rawgit.com/donkirkby/hoodlegon/master/six_star.svg
[hyacinth]: https://rawgit.com/donkirkby/hoodlegon/master/hyacinth.svg
