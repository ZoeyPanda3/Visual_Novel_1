# game/goddess_intro.rpy
# Canonical prologue owner. Ensure no other file defines `label prologue_intro`.

label prologue_intro:

    # Try a looping cosmic video; otherwise use a still; otherwise fade to black.
    $ cosmos_video = "videos/cosmos.webm"
    $ cosmos_still = "images/cosmos_bg.png"

    if renpy.exports.loadable(cosmos_video):
        call start_video_bg(path=cosmos_video)
    elif renpy.exports.loadable(cosmos_still):
        scene expression cosmos_still
    else:
        scene black

    with fade

    # Optional concealed sprite if present.
    $ goddess_silhouette = "images/goddess_mystery.png"
    if renpy.exports.loadable(goddess_silhouette):
        show expression goddess_silhouette at truecenter

    # Opening lines
    g "You do not belong here… and yet, here you stand."
    g "A fragile soul, trembling on the edge of truth and shadow."
    g "Tell me… will you be my lie, or will you chase your own truth?"

    menu:
        "Yield to the voice":
            g "Wise. Even lies, in the right hands, can be a path."
        "Resist the pull":
            g "Defiance. How bright your spark burns—for now."

    call stop_video_bg

    if renpy.has_label("chapter_1"):
        jump chapter_1
    else:
        return
