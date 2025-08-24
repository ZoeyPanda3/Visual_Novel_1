# game/goddess_font_test.rpy
# Expects the font at: game/assests/fonts/FreakySmoke.otf
# (If your folder is actually named "assets", change the path below.)

init:
    # Define a custom style for the goddess intro text
    style goddess_text is default:
        font "assests/fonts/FreakySmoke.otf"
        size 56
        color "#FFFFFF"
        outlines [(2, "#000000", 0, 0)]
        text_align 0.5
        layout "subtitle"  # keeps centered/wrapped nicely

label goddess_font_test:
    # Pure black screen; hide the normal dialogue window
    $ _window = False
    scene black
    window hide

    # Sentence 1
    show expression Text("Test sentence 1", style="goddess_text") as t1 at truecenter with Dissolve(0.8)
    pause 1.4
    hide t1 with Dissolve(0.8)
    pause 0.2

    # Sentence 2
    show expression Text("Test sentence 2", style="goddess_text") as t2 at truecenter with Dissolve(0.8)
    pause 1.4
    hide t2 with Dissolve(0.8)
    pause 0.2

    # Sentence 3
    show expression Text("Test sentence 3", style="goddess_text") as t3 at truecenter with Dissolve(0.8)
    pause 1.4
    hide t3 with Dissolve(0.8)

    # Restore the normal dialogue window afterward
    $ _window = True
    return
