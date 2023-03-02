
label start:
    scene expression "#fff"
    "Let's draw!"
    $ my_drawing = draw_logic.Draw.main(
        reference="gui/window_icon.png",
        start_width=5,
        start_color="#a00",
        xsize=800,
        ysize=600
    )
    show expression my_drawing:
        align (.5, .5)
    "It's beautiful."
    return
