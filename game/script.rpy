# game/script.rpy
# -------------------------------------------------------------------
# Entry point for the game. Routes through the prologue intro and then
# into the character customization flow.

label start:
    # Prologue intro: black screen -> 3 styled lines -> video bg -> goddess speaks
    call prologue_intro

    # Character creator: name, gender, class (returns to caller when done)
    call customization_flow

    # Continue to your next scene/label (e.g., chapter_1)
    # jump chapter_1
    return
