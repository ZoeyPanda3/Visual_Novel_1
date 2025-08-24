# game/features/goddess_intro.rpy
label goddess_intro:
    scene black with fade
    # Safe if missing; if the path doesn't exist, the game still runs fine.
    $ renpy.music.play("audio/stings/void_sting.ogg", if_changed=True)

    show silk_text "How curious… a soul adrift where none should be." at silk_reveal(0.58)
    with dissolve_slow
    $ renpy.pause(1.6)
    hide silk_text with silk_out
    $ renpy.pause(0.2)

    show silk_text "No tether. No fate. And yet… you shine." at silk_reveal(0.58)
    with dissolve_slow
    $ renpy.pause(1.6)
    hide silk_text with silk_out
    $ renpy.pause(0.2)

    show silk_text "Tell me, wanderer—what are you? A mistake… or a promise?" at silk_reveal(0.58)
    with dissolve_slow
    $ renpy.pause(1.8)
    hide silk_text with silk_out
    $ renpy.pause(0.25)

    show silk_text "I could unmake you with a thought… but perhaps… I’ll give you a choice instead." at silk_reveal(0.64)
    with dissolve_slow
    $ renpy.pause(1.9)
    hide silk_text with silk_out
    $ renpy.pause(0.25)

    show silk_text "Shape yourself before me. Let us see what kind of soul dares trespass in my domain." at silk_reveal(0.68)
    with dissolve_slow
    $ renpy.pause(2.0)
    hide silk_text with silk_out
    $ renpy.pause(0.2)

    jump character_creation
