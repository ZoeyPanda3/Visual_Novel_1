# game/customization_flow.rpy
# Logic wrapper around the customization screen. Keeps the screen lean.

label character_customization:
    $ result = renpy.call_screen("character_creator")

    if result:
        $ persistent.did_customize = True
        $ renpy.save_persistent()
        "You are [player_name], a [player_sex] [player_class]."
        jump prologue_intro
    else:
        "You hesitate, and the darkness presses in..."
        return
