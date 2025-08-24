# game/features/goddess_intro.rpy
# --------------------------------
# Prologue intro and initial back-and-forth with Nyxara

label prologue_intro:
    scene bg_cosmos_void with fade_long
    show nyxara_silhouette at truecenter with fade_mid

    # Opening lines (regal, alluring, cryptic)
    nyx "A lone soul drifts into my dominion... how curious."
    nyx "Few dare the embrace of shadow, and yet—here you are: unbidden, unveiled."
    nyx "Shall I weave you into my lies... or will you prove bold enough to seek the truth I conceal?"

    # Short back-and-forth
    $ _line = inner_voice("Where am I... and who is she?")
    n "[_line]"
    nyx "Names, places... such fragile anchors. You stand between what is spoken and what is hidden."
    nyx "Answer, little spark: do you wish to be... or merely seem?"

    # Keep menu labels strictly ASCII to avoid parser issues.
    menu:
        "I want the truth, even if it burns":
            nyx "Courage tastes sweet on mortal tongues. Very well. We shall begin."
        "If seeming keeps me alive, I'll wear any mask":
            nyx "Pragmatism. A serviceable lie. You may yet amuse me."
        "I don't owe you answers":
            nyx "Defiance, here? How quaint. Keep it—if you can."

    nyx "Before I cast you into the waking tapestry, choose the shape of your mask. Flesh must be named. Desire must be tinted. Lies must be fitted."
    hide nyxara_silhouette with fade_short

    # Hand off to customization flow.
    jump customization_entry
