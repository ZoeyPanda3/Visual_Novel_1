# game/core/styles.rpy
# Font is optional; Ren'Py will use default if the file isn't there.
define gui.goddess_font = "fonts/your_elegant_serif.ttf"

style goddess_text is default:
    size 50
    color "#EDE6FF"  # pale violet-white
    outlines [ (2, "#6A56FF33", 0, 0), (6, "#00000026", 0, 0) ]  # inner glow + soft shadow
    font gui.goddess_font
    kerning 1
    line_spacing 1
    textalign 0.5
    xalign 0.5
    yalign 0.5

style goddess_window is default:
    background None
    xfill True
    yfill True
    padding (0, 0)