# game/core/transforms.rpy
init python:
    dissolve_slow = Dissolve(0.8, alpha=True)

transform silk_reveal(center_y=0.58):
    xalign 0.5
    yalign center_y
    alpha 0.0
    blur 8.0
    zoom 1.02
    easein 0.8 alpha 1.0 blur 0.0
    # gentle breathing brightness shimmer (very subtle)
    parallel:
        0.6
        block:
            linear 0.9 matrixcolor BrightnessMatrix(0.06)
            linear 0.9 matrixcolor BrightnessMatrix(0.00)
            repeat

transform silk_out:
    linear 0.45 alpha 0.0 blur 4.0
