
init python:

    draw_logic.COLOR_CIRCLE = im.MatrixColor(
        draw_logic.COLOR_CIRCLE,
        im.matrix.colorize("#FF0000", "#E34234")
    )

label start:
    scene expression "#fff"
    "Let's draw!"
    $ my_drawing = draw_logic.Draw.main()
    show expression my_drawing
    "It's beautiful."
    return
