# RenPyDraw

__________________

## Простенькое рисование на движке Ren'Py.

Для использования, скопируйте файл `_draw.rpy` в свой проект и работайте с пространством имён `draw_logic`.

Основная функция для использования - `draw_logic.Draw.main`.
Она принимает опциональный аргумент - `background`, который будет "холстом" для рисунка.
Если аргумент не передан, в качестве фона используется заливка сервым цветом.

Так же принимаются параметры класса `Transform`, они будут применены к `background`, в случае их присутствия.

__________________

## A simple drawing on the Ren'Py engine.

To use, copy the file `_draw.rpy` into your project and work with the namespace `draw_logic`.

The main function to use is `draw_logic.Draw.main`.
It takes an optional argument, `background`, which will be the "canvas" for the drawing.
If the argument is not passed, a gray fill is used as the background.

It also accepts parameters of the `Transform` class, and they will be applied to the `background`, if they are present.

__________________

```renpy
# Simple example
label start:
    "Let's draw!"
    $ my_drawing = draw_logic.Draw.main()
    show expression my_drawing
    "It's beautiful."
    return

```

