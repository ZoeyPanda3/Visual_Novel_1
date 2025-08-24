# game/script.rpy
# Entry point. Keep this as the ONLY file that defines `label start:`.

label start:
    if not getattr(persistent, "did_customize", False):
        jump character_customization
    else:
        jump prologue_intro
