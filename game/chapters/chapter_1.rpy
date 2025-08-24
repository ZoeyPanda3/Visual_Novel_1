# game/chapters/chapter_1.rpy
# --------------------------------
# Chapter 1 entry label (handoff target after confirmation)

label chapter_1_start:
    scene bg_cosmos_void with fade_long
    show nyxara_revealed at truecenter with dissolve

    nyx "Go on then, [player_name]. Be my lie... or become your own truth."

    hide nyxara_revealed
    scene black with fade_short

    # Placeholder narration to prove the handoff works:
    $ hook = overlay_traits.get("overlay", "???").capitalize()
    n "(Form: [player_gender.capitalize()] • Path: [hook] • Name: [player_name])"

    # Continue Chapter 1 content here...
    return
