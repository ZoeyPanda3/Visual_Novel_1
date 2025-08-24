# game/script.rpy
# Single, central entry point. Safe to keep for the Launcher shortcut.
label start:
    call goddess_intro        # from features/goddess_intro.rpy
    jump prologue_after_cc    # lives in story/prologue.rpy