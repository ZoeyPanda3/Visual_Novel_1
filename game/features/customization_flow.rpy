# game/features/customization_flow.rpy
# -------------------------------------------------------------------
# Simple flow that opens the character creator and continues based on result.

label customization_flow:
    $ result = renpy.call_screen("character_creator")
    if result:
        # Selections confirmed; continue your story entry point here.
        # Example: jump chapter_1
        return
    else:
        # Player cancelled; safely return to caller (or reopen screen).
        return
